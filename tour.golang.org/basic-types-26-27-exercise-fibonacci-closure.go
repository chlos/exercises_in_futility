package main

import "fmt"

// fibonacci is a function that returns
// a function that returns an int.
func fibonacci() func() int {
    prev_fib, current_fib := 0, 1

    return func() int {
        new_fib := prev_fib + current_fib
        current_fib = prev_fib
        prev_fib = new_fib
        return current_fib

    }
}

func main() {
    f := fibonacci()
    for i := 0; i < 10; i++ {
        fmt.Println(f())
    }
}
