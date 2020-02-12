package main

import (
    "io"
    "os"
    "strings"
)

type rot13Reader struct {
    r io.Reader
}

func decode(ch byte) byte {
    if (ch >= 'a' && ch <= 'm') || (ch >= 'A' && ch <= 'M') {
        return ch + 13
    } else {
        return ch - 13
    }
}

func (r13 *rot13Reader) Read(b []byte) (int, error) {
    n, err := r13.r.Read(b)
    for i := 0; i < n; i++ {
        b[i] = decode(b[i])
    }
    return n, err
}

func main() {
    s := strings.NewReader("Lbh penpxrq gur pbqr!")
    r := rot13Reader{s}
    io.Copy(os.Stdout, &r)
}
