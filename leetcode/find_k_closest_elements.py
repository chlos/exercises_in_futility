class Solution:
    def binsearch(self, arr, x):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == x:
                return mid
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1

        return left

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr

        # let's find the closest arr[i] to X
        closest_i = self.binsearch(arr, x)

        # let's use the windows to find k closest elements
        left = closest_i - 1
        right = left + 1
        # While the sliding window's size is less than k
        while right - left - 1 < k:
            # check for out of bounds
            if left == -1:
                right += 1
                continue

            # Expand the window towards the side with the closer number
            # Be careful to not go out of bounds with the pointers
            # |a - num| < |b - num|,
            # |a - num| == |b - num|
            if (
                right == len(arr) or
                abs(arr[left] - x) <= abs(arr[right] - x)
            ):
                left -= 1
            else:
                right += 1

        # Return the window
        return arr[left + 1:right]