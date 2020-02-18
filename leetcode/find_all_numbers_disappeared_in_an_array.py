class Solution(object):
    # naive n**2 solution
    def findDisappearedNumbersNaive(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in xrange(1, len(nums) + 1):
            if i not in nums:
                result.append(i)
        return result

    # counters; additional space
    def findDisappearedNumbersCounters(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        result = []
        for n in xrange(1, len(nums) + 1):
            print n, counter[n]
            if counter[n] == 0:
                result.append(n)
        return result

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in xrange(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        for i in xrange(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result


s = Solution()
r = s.findDisappearedNumbers([1, 1])
# assert r == [2]
