package main

import (
    "golang.org/x/tour/tree"
    "fmt"
)

// Walk walks the tree t sending all values
// from the tree to the channel ch.
func Walk(t *tree.Tree, ch chan int) {
    defer close(ch)

    var dfs func(t *tree.Tree)
    dfs = func(t *tree.Tree) {
        if t == nil {
            return
        }
        dfs(t.Left)
        ch <- t.Value
        dfs(t.Right)
    }

    dfs(t)
}

// Same determines whether the trees
// t1 and t2 contain the same values.
func Same(t1, t2 *tree.Tree) bool {
    ch1, ch2 := make(chan int), make(chan int)
    go Walk(t1, ch1)
    go Walk(t2, ch2)

    val1, val2, ok1, ok2 := 0, 0, true, true
    for ok1 && ok2 {
        val1, ok1 = <- ch1
        val2, ok2 = <- ch2
        if (ok1 != ok2) || (val1 != val2) {
            return false
        }
    }

    return true
}

func main() {
    t1 := tree.New(5)
    t2 := tree.New(5)
    is_same := Same(t1, t2)
    fmt.Println("is_same:", is_same)

    t1 = tree.New(5)
    t2 = tree.New(1)
    is_same = Same(t1, t2)
    fmt.Println("is_same:", is_same)

    t1 = tree.New(5000)
    t2 = tree.New(5000)
    is_same = Same(t1, t2)
    fmt.Println("is_same:", is_same)
}
