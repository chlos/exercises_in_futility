class Solution:
    # two pass (two directions)
    # space O(n)
    # see also: https://leetcode.com/problems/candy/solutions/1300194/python-o-n-time-solution-explained/
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) <= 1:
            return len(ratings)
        
        candies = [1] * len(ratings)

        # The first loop makes sure children with a higher rating get more candy than its left neighbor
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # the second loop makes sure children with a higher rating get more candy than its right neighbor
        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candies[i - 1] = max(candies[i - 1], candies[i] + 1)

        return sum(candies)


# see the space O(1) "peaks and valleys"/"slopes" solution:
# https://leetcode.com/problems/candy/solutions/2234434/c-o-n-time-o-1-space-full-explanation/