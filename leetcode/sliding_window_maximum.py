#!/usr/bin/env python3

from collections import deque
from typing import List


class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max = []

    def Push(self, a):
        self.__stack.append(a)
        if not self.__max or a >= self.__max[-1]:
            self.__max.append(a)

    def Pop(self):
        assert(len(self.__stack))
        pop_val = self.__stack.pop()
        if self.__max and self.__max[-1] == pop_val:
            self.__max.pop()

        return pop_val

    def Max(self):
        assert(len(self.__stack))
        return self.__max[-1]

    def Empty(self):
        if self.__stack:
            return False
        else:
            return True


class QueueWithMax():
    def __init__(self):
        self.__stack_in = StackWithMax()
        self.__stack_out = StackWithMax()

    def Push(self, val):
        self.__stack_in.Push(val)

    def Pop(self):
        if self.__stack_out.Empty():
            while not self.__stack_in.Empty():
                self.__stack_out.Push(self.__stack_in.Pop())
        return self.__stack_out.Pop()

    def Max(self):
        if self.__stack_out.Empty():
            return self.__stack_in.Max()
        elif self.__stack_in.Empty():
            return self.__stack_out.Max()
        else:
            return max(self.__stack_out.Max(), self.__stack_in.Max())


class Solution:
    def maxSlidingWindow_QueueWithMax(self, nums: List[int], k: int) -> List[int]:
        maximums = []
        q = QueueWithMax()

        for i in range(k):
            q.Push(nums[i])
        maximums.append(q.Max())

        for i in range(k, len(nums)):
            q.Pop()
            q.Push(nums[i])
            maximums.append(q.Max())

        return maximums

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maximums = []
        # deque with num indeces
        q = deque()

        for i in range(len(nums)):
            # check q size vs window size
            if q and q[0] < i - k + 1:
                q.popleft()

            # pop elements which will not be maximums in current window
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            if i >= k - 1:
                maximums.append(nums[q[0]])

        return maximums