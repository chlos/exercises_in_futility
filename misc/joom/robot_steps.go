// create async controllers for robot's legs
// they should work in turn: L-R-L-R-...

func LeftLegController(interfaceCh bool) {
    for (;;) {
        for msg := range interfaceCh {
            if msg == true {
                break
            }
        }
        move(0)
        interfaceCh <- true
    }
}

func RightLegController(interfaceCh bool) {
    for (;;) {
        for msg := range interfaceCh {
            if msg == true {
                break
            }
        }
        move(1)
        interfaceCh <- true
    }
}

func RunRobot(ch chan) {
    leftIfaceCh := make(chan, bool)
    rightIfaceCh := make(chan, bool)
    go LeftLegController(rightIfaceCh)
    go RightLegController(leftIfaceCh)
}