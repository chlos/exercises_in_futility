package main

import (
    "fmt"
)

const SQRT_STEP_LIMIT = 100

func Sqrt(x float64) float64 {
    fmt.Println("x =", x)
    var root_curr = 1.0
    var root_prev float64
    for i := 0; i < SQRT_STEP_LIMIT && root_prev != root_curr; i++ {
        root_prev = root_curr
        root_curr -= (root_curr * root_curr - x) / (2 * root_curr)
        fmt.Println("root_prev =", root_prev)
    }

    return root_prev
}

func main() {
    fmt.Println(Sqrt(36 * 36))
    // fmt.Println(Sqrt(2))
}
