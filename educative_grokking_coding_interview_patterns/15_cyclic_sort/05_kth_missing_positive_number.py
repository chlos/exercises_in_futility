class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # cyclic sort
        i = 0
        while i < len(arr):
            i_val = arr[i]

            if i_val - 1 == i or i_val > len(arr):
                i += 1
                continue

            arr[i], arr[i_val - 1] = arr[i_val - 1], arr[i]

        count = 0
        current_missing = 0

        # count missing positives within the array
        other_nums = []
        for i in range(len(arr)):
            current_missing = i + 1 # candidate

            if arr[i] - 1 != i:
                count += 1
                other_nums.append(arr[i])

            if count == k:
                return current_missing

        # check the numbers outside of the array
        while count < k:
            current_missing += 1

            if current_missing not in other_nums:
                count += 1

        return current_missing