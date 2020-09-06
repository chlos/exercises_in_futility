#!/usr/bin/env python3


def nums_div_by_x(nums_start, nums_end, divs):
    count = 0
    for n in range(nums_start, nums_end + 1):
        for divider in divs:
            if n % divider == 0:
                count += 1
                break

    return count


if __name__ == "__main__":
    print(nums_div_by_x(1, 2003, [6]))
    print(nums_div_by_x(1, 2003, [7]))
    print(nums_div_by_x(1, 2003, [8]))
    print(nums_div_by_x(1, 2003, [6, 7, 8]))

    print(nums_div_by_x(1, 10, [2, 4]))