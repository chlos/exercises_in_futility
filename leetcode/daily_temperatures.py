# let's use monotonic stack - decreasing - scan days from right to left
# explaination: https://1e9.medium.com/monotonic-queue-notes-980a019d5793
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        mono_stack = collections.deque()

        mono_stack.append(len(temperatures) - 1)
        for i in reversed(range(len(temperatures) - 1)):
            while mono_stack and temperatures[mono_stack[-1]] <= temperatures[i]:
                mono_stack.pop()
            if mono_stack:
                res[i] = mono_stack[-1] - i
            mono_stack.append(i)

        return re