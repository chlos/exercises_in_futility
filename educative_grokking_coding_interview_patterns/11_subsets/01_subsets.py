def is_bit_set(num, bit):
    x = (1 << bit) & num
    if x == 0:
        return False
    return True


class Solution:
    # cascading
    def subsets_bruteforce(self, nums: List[int]) -> List[List[int]]:
        sets = [[]]
        for n in nums:
            tmp_sets = []
            for curr_set in sets:
                tmp_sets.append(curr_set + [n])
            sets.extend(tmp_sets)

        return sets

    # bitmask
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = []
        if not nums:
            return [[]]

        for bitmask in range(2 ** len(nums)):
            curr_set = []
            for num_i in range(len(nums)):
                if is_bit_set(bitmask, bit=num_i):
                    curr_set.append(nums[num_i])
            sets.append(curr_set)

        return set
