# You are given the two sorted arrays list1 and list2. Merge the two lists in a one-sorted list.

# Input: 
# list1 = [1,2,4], 
# list2 = [1,3,4] 
# Output: [1,1,2,3,4,4]

# Input: 
# list1 = [], 
# list2 = [0] 
# Output: [0]

def merge_arrays(list1, list2):
    result = []
    idx_1, idx_2 = 0, 0

    if not list1:
        return list2
    if not list2:
        return list1

    while idx_1 < len(list1) and idx_2 < len(list2):
        if list1[idx_1] < list2[idx_2]:
            result.append(list1[idx_1])
            idx_1 += 1
        elif list1[idx_1] > list2[idx_2]:
            result.append(list2[idx_2])
            idx_2 += 1
        else:
            result.append(list1[idx_1])
            result.append(list2[idx_2])
            idx_1 += 1
            idx_2 += 1

    curr_idx = 0
    l = []
    if idx_1 == len(list1) - 1:
        l = list1
        curr_idx = idx_1
    else:
        l = list2
        curr_idx = idx_2
    for idx in range(curr_idx, len(l)):
        result.append(l[idx])

    return result


def test_1(msg, list1, list2, expected):
    print(msg)
    result = merge_arrays(list1, list2)
    print(result, expected)
    assert result == expected
    print('ok\n')


test_1("test1", [1,2,4], [1, 3, 4], [1,1,2,3,4,4])
test_1("test5", [1], [1, 3, 4], [1, 1, 3, 4])
test_1("test2", [], [1, 3, 4], [1, 3, 4])
test_1("test3", [1,2,4], [], [1, 2, 4])
test_1("test4", [], [], [])
test_1("test6", [1], [2], [1, 2])
test_1("test7", [2], [1], [1, 2])