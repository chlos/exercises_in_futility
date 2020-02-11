package main

import (
    "fmt"
)

const SQRT_STEP_LIMIT = 100

type ErrNegativeSqrt float64

func (e ErrNegativeSqrt) Error() string {
    return fmt.Sprintf("cannot Sqrt negative number: %v", float64(e))
}

func Sqrt(x float64) (float64, error) {
    fmt.Println("x =", x)
    if x < 0 {
        return 0.0, ErrNegativeSqrt(x)
    }

    var root_curr = 1.0
    var root_prev float64
    for i := 0; i < SQRT_STEP_LIMIT && root_prev != root_curr; i++ {
        root_prev = root_curr
        root_curr -= (root_curr * root_curr - x) / (2 * root_curr)
    }

    return root_prev, nil
}

func main() {
    fmt.Println(Sqrt(2))
    fmt.Println(Sqrt(-2))
}
