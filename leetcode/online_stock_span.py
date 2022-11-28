# monotonic stack
# https://leetcode.com/problems/online-stock-span/solutions/640358/java-solution-with-visualization-and-easy-explained/
# see the diagram
class StockSpanner:

    def __init__(self):
        self.mono = collections.deque()
        
    def next(self, price: int) -> int:
        curr_span = 1
        while self.mono and self.mono[-1][0] <= price:
            _, prev_span = self.mono.pop()
            curr_span += prev_span
        self.mono.append((price, curr_span))

        return curr_span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)