# knapsack problem
# https://leetcode.com/discuss/study-guide/1152328/01-Knapsack-Problem-and-Dynamic-Programming
# https://leetcode.com/discuss/study-guide/1308617/Dynamic-Programming-Patterns

# https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/solutions/654490/dp-is-easy-5-step-dp-thinking-process-explained/
# dfs recursive top down; timout without memo/caching; let's use python's caching
class Solution:
    @cache
    def dfs(self, digit, target_remaining):
        # base cases
        if target_remaining == 0:
            # we found target integer, ok!
            return ''
        if target_remaining < 0 or digit >= len(self.cost) + 1:
            # rules are broken
            return '0'

        # take the current digit to the result
        # reset the index back to 1 in order to choose from the whole slate of 1-9 numbers again
        take = str(digit) + self.dfs(1, target_remaining - self.cost[digit - 1])
        # we simply increment the index aka try the next number
        skip = self.dfs(digit + 1, target_remaining)
        return self.getMax(take, skip)

    def getMax(self, num1, num2):
        if '0' in num1:
            return num2
        elif '0' in num2:
            return num1

        if int(num1) > int(num2):
            return num1
        else:
            return num2

    def largestNumber(self, cost: List[int], target: int) -> str:
        self.cost = cost
        result = self.dfs(0, target)
        if '0' in result:
            return '0'
        else:
            return result


# bottom up DP:
# https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/solutions/635189/c-dp-with-explanation/