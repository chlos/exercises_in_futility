#!/usr/bin/env python3

from collections import namedtuple


Point = namedtuple('Point', ['x', 'y'])


def get_data():
    data = input().split()

    n = int(data[0])
    print(n)    # FIXME

    vertices = []
    i = 1
    while i < n * 2:
        vertex = Point(float(data[i]), float(data[i + 1]))
        vertices.append(vertex)
        i += 2
    print(vertices)     # FIXME

    point = Point(float(data[-2]), float(data[-1]))
    print(point)     # FIXME

    return vertices, point


def is_point_in_polygon(vertices, point):
    is_inside = False

    i = -1
    while i < len(vertices) - 1:
        v1 = vertices[i]
        v2 = vertices[i + 1]
        i += 1

        if point == v1 or point == v2:
            # point is one of vertices
            return True

        if point.y <= min(v1.y, v2.y) or point.y >= max(v1.y, v2.y):
            continue

        x_int = v1.x + (v2.x - v1.x) * (point.y - v1.y) / (v2.y - v1.y)
        if x_int <= point.x:
            is_inside = not is_inside

    return is_inside


def test_is_point_in_polygon(f):
    vs = [Point(x=0.0, y=0.0), Point(x=3.0, y=0.0), Point(x=0.0, y=3.0)]
    p = Point(x=1.0, y=1.0)
    assert f(vs, p)

    vs = [Point(x=0.0, y=0.0), Point(x=3.0, y=0.0), Point(x=0.0, y=3.0)]
    p = Point(x=0.0, y=1.0)
    assert f(vs, p)

    vs = [Point(x=0.0, y=0.0), Point(x=4.0, y=0.0), Point(x=1.0, y=1.0), Point(x=0.0, y=4.0)]
    p = Point(x=1.5, y=1.5)
    assert not f(vs, p)


if __name__ == "__main__":
    test_is_point_in_polygon(is_point_in_polygon)

    vertices, point = get_data()

    is_pip = is_point_in_polygon(vertices, point)
    if is_pip:
        print('YES')
    else:
        print('NO')