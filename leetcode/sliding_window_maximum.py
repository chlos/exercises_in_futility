#!/usr/bin/env python3

import collections
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
    def maxSlidingWindow_bruteForce(self, nums: List[int], k: int) -> List[int]:
        result = []

        window = collections.deque()
        for i in range(k):
            window.append(nums[i])
        window_max = max(window)
        result.append(window_max)
        
        for i in range(k, len(nums)):
            window.popleft()
            window.append(nums[i])
            window_max = max(window)
            result.append(window_max)

        return result

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

    # BEST!
    # https://leetcode.com/problems/sliding-window-maximum/solutions/871317/clear-thinking-process-with-picture-brute-force-to-mono-deque-python-java-javascript/
    # https://algo.monster/problems/sliding_window_maximum
    def maxSlidingWindow_monotonicDeque(self, nums: List[int], k: int) -> List[int]:
        result = []

        # we store indices instead of actual elements in the deque.
        # This is because we need the index to know if an element is out of the window
        # or not and we can always get the value using the index from the array
        window = collections.deque()
        for i, n in enumerate(nums):
            # remove first element if it's outside the window
            if window and window[0] <= i - k:
                window.popleft()

            # when we push an element into the deque,
            # we first pop everything smaller than it out of the deque
            while window and nums[window[-1]] <= n:
                window.pop()
            window.append(i)

            # we have full k-window
            if i >= k-1:
                result.append(nums[window[0]])

        return result