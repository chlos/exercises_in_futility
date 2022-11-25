class Solution:
    # mono stack/queue/deque again
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        greater_map = {}
        mono_deque = collections.deque()

        # keep "small" nums in mono, until we meet "greater" num
        for n2 in nums2:
            # pop every "smaller then current n2" nums
            # n2 is their "next greater element"
            while mono_deque and n2 > mono_deque[-1]:
                small_n = mono_deque.pop()
                greater_map[small_n] = n2
                print(small_n, n2)
            mono_deque.append(n2)

        # there is no next greater element for these nums
        while mono_deque:
            small_n = mono_deque.popleft()
            greater_map[small_n] = -1

        for n1 in nums1:
            ans.append(greater_map[n1])

        return ans