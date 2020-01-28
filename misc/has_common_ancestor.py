#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Suppose we have some input data describing a graph of relationships between parents and children over multiple generations.
The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

For example, in this diagram, 6 and 8 have a common ancestor of 4.

         14  13
         |   |
1   2    4   12
 \ /   / | \ /
  3   5  8  9
   \ / \     \
    6   7     11

parentChildPairs1 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)
]

Write a function that takes the graph, as well as two of the individuals in our dataset, as its inputs and returns true if and only if they share at least one ancestor.

Sample input and output:

hasCommonAncestor(parent_child_pairs_1, 3, 8) => false
hasCommonAncestor(parent_child_pairs_1, 5, 8) => true
hasCommonAncestor(parent_child_pairs_1, 6, 8) => true
hasCommonAncestor(parent_child_pairs_1, 6, 9) => true
hasCommonAncestor(parent_child_pairs_1, 1, 3) => false
hasCommonAncestor(parent_child_pairs_1, 7, 11) => true
hasCommonAncestor(parent_child_pairs_1, 6, 5) => true
hasCommonAncestor(parent_child_pairs_1, 5, 6) => true

Additional example: In this diagram, 4 and 12 have a common ancestor of 11.

        11
       /  \
      10   12
     /  \
1   2    5
 \ /    / \
  3    6   7
   \        \
    4        8

parentChildPairs2 = [
    (11, 10), (11, 12), (10, 2), (10, 5), (1, 3),
    (2, 3), (3, 4), (5, 6), (5, 7), (7, 8),
]

hasCommonAncestor(parentChildPairs2, 4, 12) => true
hasCommonAncestor(parentChildPairs2, 1, 6) => false
hasCommonAncestor(parentChildPairs2, 1, 12) => false
'''
from collections import defaultdict

parent_child_pairs_1 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)
]

parent_child_pairs_2 = [
    (11, 10), (11, 12), (10, 2), (10, 5), (1, 3),
    (2, 3), (3, 4), (5, 6), (5, 7), (7, 8)
]

parent_child_pairs_3 = [
    (1, 2), (1, 3), (2, 4), (5, 4),
]


def getAncestorsMap(pairs, child):
    ancestors_map = defaultdict(list)
    for current_parent, current_child in pairs:
        ancestors_map[current_child].append(current_parent)
    return ancestors_map


def getAncestorsSet(ancestors_map, child):
    ancestors_set = set()
    current_children = []
    current_children.append(child)
    print 'ancestors_map: ', ancestors_map
    while True:
        current_parents = []
        for current_child in current_children:
            print 'current_child: ', current_child
            p = ancestors_map.get(current_child)
            if p is not None:
                current_parents += p
        if not current_parents:
            break
        current_children = []
        current_children += current_parents
        for current_parent in current_parents:
            ancestors_set.add(current_parent)

    return ancestors_set


def hasCommonAncestor(pairs, child_1, child_2):
    child_1_map = getAncestorsMap(pairs, child_1)
    child_2_map = getAncestorsMap(pairs, child_2)
    child_1_ancestors = getAncestorsSet(child_1_map, child_1)
    child_2_ancestors = getAncestorsSet(child_2_map, child_2)
    common_ancestors = child_1_ancestors.intersection(child_2_ancestors)
    if common_ancestors:
        return True
    else:
        return False

test_map = getAncestorsMap(parent_child_pairs_3, 4)
assert dict(test_map) == {2: [1], 3: [1], 4: [2, 5]}
print test_map
hasCommonAncestor(parent_child_pairs_3, 4, 2)
print 'getAncestorsMap() OK'

test_set = getAncestorsSet(test_map, 3)
print test_set
assert test_set == {1}
test_set = getAncestorsSet(test_map, 4)
print test_set
assert test_set == {1, 2, 5}
print 'getAncestorsSet() OK'

test_common = hasCommonAncestor(parent_child_pairs_3, 4, 3)
print test_common
assert test_common
test_common = hasCommonAncestor(parent_child_pairs_3, 5, 3)
print test_common
assert not test_common

parentChildPairs2 = [
    (11, 10), (11, 12), (10, 2), (10, 5), (1, 3),
    (2, 3), (3, 4), (5, 6), (5, 7), (7, 8),
]
t = hasCommonAncestor(parentChildPairs2, 4, 12)
assert t
t = hasCommonAncestor(parentChildPairs2, 1, 6)
assert not t
t = hasCommonAncestor(parentChildPairs2, 1, 12)
assert not t


parentChildPairs1 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)
]

t = hasCommonAncestor(parent_child_pairs_1, 3, 8)
assert t == False
t = hasCommonAncestor(parent_child_pairs_1, 5, 8)
assert t == True
t = hasCommonAncestor(parent_child_pairs_1, 6, 8)
assert t == True
t = hasCommonAncestor(parent_child_pairs_1, 6, 9)
assert t == True
t = hasCommonAncestor(parent_child_pairs_1, 1, 3)
assert t == False
t = hasCommonAncestor(parent_child_pairs_1, 7, 11)
assert t == True
t = hasCommonAncestor(parent_child_pairs_1, 6, 5)
assert t == True
t = hasCommonAncestor(parent_child_pairs_1, 5, 6)
assert t == True

print 'hasCommonAncestor() OK'
