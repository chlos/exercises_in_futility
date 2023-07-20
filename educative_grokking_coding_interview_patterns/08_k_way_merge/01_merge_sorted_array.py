# Three Pointers (Start From the End)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = m + n - 1
        idx1 = m - 1
        idx2 = n - 1
        while idx >= 0:
            if idx2 < 0:
                break

            if idx1 >= 0 and nums1[idx1] > nums2[idx2]:
                nums1[idx] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[idx] = nums2[idx2]
                idx2 -= 1

            idx -= 1