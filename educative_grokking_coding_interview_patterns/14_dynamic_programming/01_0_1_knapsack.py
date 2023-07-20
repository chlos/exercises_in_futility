# https://leetcode.com/discuss/study-guide/1152328/01-Knapsack-Problem-and-Dynamic-Programming
def find_max_knapsack_profit_2d(capacity, weights, values):
    # dp matrix:
    #         cap=0   cap=1   cap=2 ...
    # weight=0
    # weight=w1
    # weight=w2
    # ...
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(weights) + 1)]

    for weight_row in range(len(weights)):
        for curr_cap in range(capacity + 1):
            # this item could fit the knapsack
            if weights[weight_row] <= curr_cap:
                # choose the most valuable option
                dp[weight_row + 1][curr_cap] = max(
                    # take the item + previous items that fit the remaining capacity
                    values[weight_row] + dp[weight_row][curr_cap - weights[weight_row]],
                    # dont take, prev items are still in the bag
                    dp[weight_row][curr_cap]
                )
            # this item doesn't fit the knapsack
            else:
                # dont take, prev items are still in the bag
                dp[weight_row + 1][curr_cap] =  dp[weight_row][curr_cap]

    return dp[-1][-1]


def find_max_knapsack_profit(capacity, weights, values):
    dp = [0 for _ in range(capacity + 1)]

    for weight_row in range(len(weights)):
        for curr_cap in range(capacity, 0, -1):
            # this item could fit the knapsack
            if weights[weight_row] <= curr_cap:
                dp[curr_cap] = max(
                    values[weight_row] + dp[curr_cap - weights[weight_row]],
                    dp[curr_cap]
                )
            else:
                break

    return dp[-1]