# https://www.youtube.com/watch?v=LPFhl65R7ww
# https://leetcode.com/problems/median-of-two-sorted-arrays/solutions/2471/very-concise-o-log-min-m-n-iterative-solution-with-detailed-explanation/
# https://leetcode.com/problems/median-of-two-sorted-arrays/solutions/2511/intuitive-python-o-log-m-n-solution-by-kth-smallest-in-the-two-sorted-arrays-252ms/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # we consider nums2 as a shorter one for simplicity
        len1, len2 = len(nums1), len(nums2)
        if len2 > len1:
            nums1, nums2 = nums2, nums1
            len1, len2 = len2, len1

        lo, hi = 0, len2 * 2
        while lo <= hi:
            mid2 = (lo + hi) / 2
            mid1 = len1 + len2 - mid2

            if mid1 == 0:
                l1 = -float('inf')
            else:
                l1 = nums1[int((mid1 - 1) // 2)]
            if mid2 == 0:
                l2 = -float('inf')
            else:
                l2 = nums2[int((mid2 - 1) // 2)]

            if mid1 == len1 * 2:
                r1 = float('inf')
            else:
                r1 = nums1[int(mid1 // 2)]
            if mid2 == len2 * 2:
                r2 = float('inf')
            else:
                r2 = nums2[int(mid2 // 2)]

            # A1's lower half is too big; need to move C1 left (C2 right)
            if l1 > r2:
                lo = mid2 + 1
            # A2's lower half too big; need to move C2 left
            elif l2 > r1:
                hi = mid2 - 1
            # Otherwise, that's the right cut
            else:
                return (max(l1, l2) + min(r1, r2)) / 2

        return -1