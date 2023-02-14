'''
Compress string:
AAABBC -> A4B2C
'''







'''
В массиве N чисел.
Определить, есть ли два числа, у которых индексы отличаются не более чем на к,
а значения не более чем на t
'''

# bruteforce
def is_close(arr, k, t):
    li = 0
    while li < len(arr):
        for ri in range(li + 1, li + k + 1):
            if ri < len(arr) and abs(arr[li] - arr[ri]) <= t:
                return True
        li += 1

    return False

'''
[1539]53545253
9[5395]3545253

k = 7 t = 3
[0 10 30 40 90 100 120] 42-t, 42+t
'''

for i = 0...k:
    window.bin_add(arr[i])
for i = k+1...len(arr):
    n = arr[1]
    window.pop(old_val)
    window. find(n - t, n - t)