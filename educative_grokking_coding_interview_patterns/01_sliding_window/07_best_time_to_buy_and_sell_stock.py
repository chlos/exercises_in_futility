def max_profit(stock_prices):
    min_price = float('inf')
    max_profit = 0

    for curr_price in stock_prices:
        min_price = min(min_price, curr_price)
        max_profit = max(max_profit, curr_price - min_price)

    return max_profit