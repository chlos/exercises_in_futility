// Design, model, and implement a client API for managing users and groups. We should implement each of these parts incrementally, each with working code and some test cases:
// 1. CRUD for Users
// 2. CRUD for User/Group many-to-many relationships (skip CRUD for Groups since this will resemble the CRUD for Users)

// While the API design should be aimed at a real-world use-case (e.g. a client API that interacts with remote services or datastores), the implementation here should be simple and in-memory and assumed to be running on a single instance, as though we were mocking this client API for testing purposes.

// We recommend first designing the API interface(s) and models. Then implementing piece by piece and running the code / testing iteratively for each piece.

package main

import "fmt"

type Group struct {
	ID string
}

type User struct {
	id   int64
	Name string
	// Groups []string
}

type UserSettings struct {
	Name string
}

type UsersCRUD struct {
	users map[int64]User
	// groups map	// load in the costructor
	ids int64
}

// ...
func (u *UsersCRUD) InsertUser(name string) error {
	u.ids++
	user := User{
		id:   u.ids,
		Name: name,
	}
	err := u.insertUserStruct(user)

	return err
}

func (u *UsersCRUD) GetUser(id int64) (User, bool) {
	user, ok := u.users[id]
	return user, ok
}

func (u *UsersCRUD) DeleteUser(id int64) bool {
	_, ok := u.users[id]
	if !ok {
		return false
	}
	delete(u.users, id)
	return true
}

func (u *UsersCRUD) UpdateUser(id int64, userSettings UserSettings) bool {
	user, ok := u.GetUser(id)
	if !ok {
		return false
	}

	user.Name = userSettings.Name
	u.users[user.id] = user

	return true
}

func (u *UsersCRUD) GetUserGroups(id int64) []User {
	return []User{}
}
func (u *UsersCRUD) GetGroupUsers(id string) []Group {
	return []Group{}
}

func (u *UsersCRUD) AddUserToGroup(id int64, id string) error {
	return nil
}
func (u *UsersCRUD) RemoveUserFromGroup(id int64, id string) error {}

func (u *UsersCRUD) insertUserStruct(user User) error {
	_, ok := u.users[user.id]
	if ok {
		return fmt.Errorf("user already esists: %v", user.id)
	}
	u.users[user.id] = user

	return nil
}

func main() {
	for i := 0; i < 5; i++ {
		fmt.Println("Hello, World!")
	}
}
