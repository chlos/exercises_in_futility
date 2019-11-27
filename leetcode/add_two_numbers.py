#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def get_number(l):
    num = 0
    mult = 1
    current_node = l
    while current_node is not None:
        current_digit = current_node.val
        current_node = current_node.next
        num += current_digit * mult
        mult *= 10
    return num


def get_list(number):
    list_head = None
    current_node = None
    if number == 0:
        return ListNode(0)
    while number:
        digit = number % 10
        if current_node is None:
            current_node = ListNode(digit)
            list_head = current_node
        else:
            current_node.next = ListNode(digit)
            current_node = current_node.next
        number = number / 10

    return list_head


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = get_number(l1)
        num2 = get_number(l2)
        sum_num = num1 + num2

        sum_list = get_list(sum_num)
        return sum_list
