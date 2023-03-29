class Solution:
    def summaryRanges_1(self, nums: List[int]) -> List[str]:
        ranges = []
        if not nums:
            return ranges

        # build ranges
        prev_num = nums[0]
        curr_range = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] - prev_num > 1:
                if curr_range[0] != prev_num:
                    curr_range.append(prev_num)
                ranges.append(curr_range)
                curr_range = [nums[i]]

            prev_num = nums[i]

        if curr_range[0] != nums[-1]:
            ranges.append(curr_range + [nums[-1]])
        else:
            ranges.append(curr_range)

        # format ranges as strings
        ranges_str = []
        for curr_range in ranges:
            if len(curr_range) == 1:
                ranges_str.append(f'{curr_range[0]}')
            else:
                ranges_str.append(f'{curr_range[0]}->{curr_range[1]}')

        return ranges_str

    # more consice
    # https://leetcode.com/problems/summary-ranges/solutions/1805321/c-0ms-100-easy-to-understand-full-explanation/
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        if not nums:
            return ranges

        # build ranges
        curr_range_start = nums[0]
        for i in range(len(nums)):
            if i == len(nums) - 1 or nums[i + 1] - nums[i] > 1:
                if nums[i] != curr_range_start:
                    ranges.append([curr_range_start, nums[i]])
                else:
                    ranges.append([curr_range_start])

                if i < len(nums) - 1:
                    curr_range_start = nums[i + 1]

        # format ranges as strings
        ranges_str = []
        for curr_range in ranges:
            if len(curr_range) == 1:
                ranges_str.append(f'{curr_range[0]}')
            else:
                ranges_str.append(f'{curr_range[0]}->{curr_range[1]}')

        return ranges_str