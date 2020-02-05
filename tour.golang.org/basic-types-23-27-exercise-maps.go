package main

import (
    "golang.org/x/tour/wc"
    "strings"
)

func WordCount(s string) map[string]int {
    wc := make(map[string]int)
    words := strings.Fields(s)
    for _, word := range words {
        wc[word] += 1
    }
    return wc
}

func main() {
    wc.Test(WordCount)
}
