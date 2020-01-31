package main

import (
    "golang.org/x/tour/pic"
)

func Pic(dx, dy int) [][]uint8 {
    dydx := make([][]uint8, dy)
    for y := range dydx {
        dydx[y] = make([]uint8, dx)
        for x := range dydx[y] {
            dydx[y][x] = uint8(x * y)
        }
    }

    return dydx
}

func main() {
    pic.Show(Pic)
}
