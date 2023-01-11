package main

type Point struct {
    X int
    Y int
}

func hasVSymmetry(points []Point) bool {
    if len(points) <= 0 {
        return false
    }

    points_map := make(map[int][]int)
    for _, p := range points {
        points_map[p.Y] = append(points_map[p.Y], p.X)
    }

    i := 0
    sym_points := make([]int, len(points_map))
    for y, xs := range points_map {
        var sym_point int
        for _, x := range xs {
            sym_point += x
        }
        sym_point = sym_point / len(xs)
        sym_points = append(sym_points, sym_point)
    }

    prev_sym_point = sym_points[0]
    for _, p := range sym_points {
        if p != prev_sym_point {
            return false
        }
    }

    return true
}
