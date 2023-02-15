# 1

# Sorted Array of N elements. Index I is given, return K closest elements to A[I]




# 2
# https://leetcode.com/problems/subarray-sum-equals-k/

# Дан массив целых чисел, нужно найти непустой подотрезок (непрерывную подпоследовательность) с заданной суммой X,
#  либо сказать, что это невозможно.
# Для найденного отрезка (если он существует) следует выдать на выход индексы его концов.

x = 7
... i = 1; part_sum = 3
i = 2; part_sum = 6
... i = 3; part_sum = 10
i = 4; part_sum = 15
# [1, 2, (3, 4,) 5]
# [1, 3,  6,  10, 15]


def find_interval(arr, x):
    sum_dict = {}
    part_sum = 0
    for i in range(len(arr)):
        part_sum += arr[i]
        sum_dict[part_sum] = i

        if part_sum == x:
            return 0, i

        needed_i = sum_dict.get(part_sum - x)
        if needed_i is not None:
            return min(i, needed_i + 1), max(i, needed_i + 1)

    return None, None