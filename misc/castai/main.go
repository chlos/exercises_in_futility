package main

import (
	"fmt"
	"sync"
	"time"
)

// 1. Cowboys shoot randomly at each other
// 2. After shot, cowboys sleeps for 1sec
// 3. Cowboys are shooting until last men standing or everyone dies
// [
//     {
//       "name": "John",
//       "health": 10,
//       "damage": 1
//     },
//     {
//       "name": "Bill",
//       "health": 8,
//       "damage": 2
//     },
//     {
//       "name": "Sam",
//       "health": 10,
//       "damage": 1
//     },
//     {
//       "name": "Peter",
//       "health": 5,
//       "damage": 3
//     },
//     {
//       "name": "Philip",
//       "health": 15,
//       "damage": 1
//     }
// ]

type CowboyData struct {
	Health int
	Damage int
}

func getCowboysData() CowboysData {
	return CowboysData{
		data: map[string]CowboyData{
			"John": {
				Health: 10,
				Damage: 1,
			},
			"Bill": {
				Health: 8,
				Damage: 2,
			},
			"Sam": {
				Health: 10,
				Damage: 1,
			},
			"Peter": {
				Health: 5,
				Damage: 3,
			},
			"Philip": {
				Health: 15,
				Damage: 1,
			},
		},
	}
}

type Bullet struct {
	TargetName string
	Damage     int
}

type CowboysData struct {
	data map[string]CowboyData
	mtx  sync.RWMutex
}

type Shooting struct {
	cowboysData  CowboysData
	cowboysAlive map[string]struct{}
	bulletsCh    chan Bullet
}

func NewShooting() (*Shooting, error) {
	cowboysData := getCowboysData()
	bulletsCh := make(chan Bullet)
	cowboysAlive := make(map[string]struct{})
	for cowboyName := range cowboysData.data {
		cowboysAlive[cowboyName] = struct{}{}
	}

	return &Shooting{
		cowboysData:  cowboysData,
		cowboysAlive: cowboysAlive,
		bulletsCh:    bulletsCh,
	}, nil
}

func (s *Shooting) Start() {
	fmt.Printf("Start\n")
	s.startCowboys()
	s.startManager()
}

func (s *Shooting) getRandomCowboyName(shooterName string) string {
	s.cowboysData.mtx.Lock()
	defer s.cowboysData.mtx.Unlock()
	for name := range s.cowboysData.data {
		if s.cowboysData.data[name].Health > 0 && name != shooterName {
			return name
		}
	}

	return ""
}

func (s *Shooting) startCowboys() {
	cowboy := func(name string) {
		for {
			s.cowboysData.mtx.Lock()
			if s.cowboysData.data[name].Health <= 0 {
				s.cowboysData.mtx.Unlock()
				return
			}
			s.cowboysData.mtx.Unlock()

			targetName := s.getRandomCowboyName(name)
			bullet := Bullet{
				TargetName: targetName,
				Damage:     s.cowboysData.data[name].Damage,
			}
			s.bulletsCh <- bullet
			fmt.Printf("%s shoots to %s with damage %d\n", name, targetName, s.cowboysData.data[name].Damage)

			time.Sleep(time.Second)
		}
	}

	for name := range s.cowboysData.data {
		go cowboy(name)
	}
}

func (s *Shooting) startManager() {
	fmt.Printf("Manager started\n")

	// go func() {
	for bullet := range s.bulletsCh {
		s.cowboysData.mtx.Lock()
		targetData := s.cowboysData.data[bullet.TargetName]
		targetData.Health -= bullet.Damage
		s.cowboysData.data[bullet.TargetName] = targetData
		s.cowboysData.mtx.Unlock()

		if targetData.Health <= 0 {
			delete(s.cowboysAlive, bullet.TargetName)
		}
		fmt.Printf("%s was shot with damage %d; now their health is %d\n", bullet.TargetName, bullet.Damage, targetData.Health)
		fmt.Printf("cowboys number: %d\n", len(s.cowboysAlive))
		if len(s.cowboysAlive) <= 1 {
			fmt.Printf("only one cowboy alive: %s\n", s.cowboysAlive)
			close(s.bulletsCh)
			return
		}
	}
	// }()
}

func main() {
	shooting, err := NewShooting()
	if err != nil {
		fmt.Printf("Shooting init error: %v", err)
		return
	}

	shooting.Start()
}
