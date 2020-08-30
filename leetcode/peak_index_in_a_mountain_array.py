#!/usr/bin/env python3

from typing import List


class Solution:
    # O(n)
    def peakIndexInMountainArray_1(self, A: List[int]) -> int:
        for i in range(1, len(A) - 1):
            if A[i - 1] < A[i] > A[i + 1]:
                return i
        return None

    # bin search, O(nlogn)
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        lo = 0
        hi = len(A) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if A[mid] < A[mid + 1]:
                lo = mid + 1
            elif A[mid - 1] > A[mid]:
                hi = mid
            else:
                return mid
        return None