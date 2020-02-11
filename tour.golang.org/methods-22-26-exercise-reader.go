package main

import "golang.org/x/tour/reader"

type MyReader struct{}

// TODO: Add a Read([]byte) (int, error) method to MyReader.
func (mr MyReader) Read(arr []byte) (int, error) {
    for i := 0; i < len(arr); i++ {
        arr[i] = 'A'
    }
    return len(arr), nil
}


func main() {
    reader.Validate(MyReader{})
}

