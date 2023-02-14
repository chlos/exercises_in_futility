'''
Нужно реализовать функцию  OneEditApart , проверяющую, можно ли одну строку получить из другой не более, 
чем за одно исправление (удаление, добавление, изменение символа):

OneEditApart("cat", "dog") -> false 
OneEditApart("cat", "cats") -> true 
OneEditApart("cat", "cut") -> true 
OneEditApart("cat", "cast") -> true 
OneEditApart("cat", "at") -> true 
OneEditApart("cat", "acts") -> false
'''


def is_fixable(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False

    fixes_needed = 0
    idx_1, idx_2 = 0, 0
    while idx_1 < len(s1) and idx_2 < len(s2):
        if s1[idx_1] == s2[idx_2]:
            idx_1 += 1
            idx_2 += 1
            continue

        fixes_needed += 1
        if fixes_needed > 1:
            return False

        if len(s1) > len(s2):
            idx_1 += 1
        elif len(s1) < len(s2):
            idx_2 += 1
        else:
            idx_1 += 1
            idx_2 += 1

    if abs(len(s1) - len(s2)) > 0 and fixes_needed > 0:
        return False

    return True

'''
-----------------------


true:

    4
   / \
  2   5
 / \
1   3

false (4 находится в левом поддереве относительно 3):

    3
   / \
  2   5
 / \
1   4
'''


class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right


def recur(node, upper, lower):
    if node is None:
        return True
    if node.val > upper or node.val < lower:
        return False

    return recur(node.left, node.val, lower) and recur(node.right, upper, node.val)


def check_tree(root):
    return recur(root, float('inf'), -float('inf'))