package main

import (
    "golang.org/x/tour/pic"
    "image"
    "image/color"
)

type Image struct{
    w int
    h int
}

func (img Image) ColorModel() color.Model {
    return color.RGBAModel
}

func (img Image) Bounds() image.Rectangle {
    return image.Rect(0, 0, img.w, img.h)
}

func (img Image) At(x, y int) color.Color {
    r := uint8(x + y)
    g := uint8(y - x)
    b := uint8(x ^ y)
    opac := uint8(x * y)
    return color.RGBA{r, g, b, opac}
}

func main() {
    m := Image{255, 255}
    pic.ShowImage(m)
}
