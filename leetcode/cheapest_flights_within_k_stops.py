# simple DFS
# timeout
class Solution_SimpleDFS:
    def buildGraph(self, flights):
        graph = collections.defaultdict(list)
        for fl_from, fl_to, fl_price in flights:
            graph[fl_from].append((fl_to, fl_price))

        return graph

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = self.buildGraph(flights)
        global cheapest_price
        cheapest_price = float('inf')

        def dfs(node, visited, curr_price, curr_stops):
            global cheapest_price

            # don't go deeper if this route is already to expensive or too long
            if curr_stops > k or curr_price >= cheapest_price:
                return

            # found one of the possible routes to dst
            if node == dst:
                cheapest_price = min(cheapest_price, curr_price)

            for node_dst, node_dst_price in graph[node]:
                if node_dst in visited:
                    continue
                visited.add(node_dst)
                found = dfs(node_dst, visited, curr_price + node_dst_price, curr_stops + 1)
                visited.remove(node_dst)

        dfs(src, {src}, 0, -1)
        if cheapest_price != float('inf'):
            return cheapest_price
        else:
            return -1


# DFS + memoization
# https://leetcode.com/problems/cheapest-flights-within-k-stops/solutions/1007689/python-dfs-memorization-with-explanantion/
class Solution_DFS_Memo:
    def buildGraph(self, flights):
        graph = collections.defaultdict(list)
        for fl_from, fl_to, fl_price in flights:
            graph[fl_from].append((fl_to, fl_price))

        return graph

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = self.buildGraph(flights)
        # (node, level) -> accumulated price
        memo = {}

        def dfs(node, curr_k):
            # distance to itself = 0
            if node == dst:
                return 0

            # we're out of stops number
            if curr_k < 0:
                return float('inf')

            # just return the saved path price if any
            if (node, curr_k) in memo:
                return memo[(node, curr_k)]

            price = float('inf')
            for node_dst, node_dst_price in graph[node]:
                price = min(price, dfs(node_dst, curr_k - 1) + node_dst_price)

            memo[(node, curr_k)] = price
            return price

        cheapest_price = dfs(src, k)
        if cheapest_price != float('inf'):
            return cheapest_price
        else:
            return -1


# Dijkstra
# https://leetcode.com/problems/cheapest-flights-within-k-stops/solutions/317262/2-clean-python-solution-bfs-dijkstra-explained/
class Solution:
    def buildGraph(self, flights):
        graph = collections.defaultdict(list)
        for fl_from, fl_to, fl_price in flights:
            graph[fl_from].append((fl_to, fl_price))

        return graph

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = self.buildGraph(flights)

        # visited[node] represents the remaining steps to reach node with the lowest cost
        visited = [0] * n

        # prioirty queue: (price_to_node, stops+1 remaining, node)
        pq = [(0, k + 1, src)]
        while pq:
            node_price, node_stops, node = heapq.heappop(pq)

            # found!
            if node == dst:
                return node_price

            # avoid loops
            if visited[node] >= node_stops:
                continue
            visited[node] = node_stops

            if node_stops > 0:
                for node_dst, node_dst_price in graph[node]:
                    heapq.heappush(pq, (node_price + node_dst_price, node_stops - 1, node_dst))

        return -1


# BFS: fastest
# https://leetcode.com/problems/cheapest-flights-within-k-stops/solutions/3099885/day-26-simple-bfs-easiest-beginner-friendly-solution/
# https://leetcode.com/problems/cheapest-flights-within-k-stops/solutions/267200/python-dijkstra/
class Solution_BFS:
    def buildGraph(self, flights):
        graph = collections.defaultdict(list)
        for fl_from, fl_to, fl_price in flights:
            graph[fl_from].append((fl_to, fl_price))

        return graph

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = self.buildGraph(flights)

        min_prices = [float('inf') for _ in range(n)]
        stops = 0   # basically it's graph's level

        queue = collections.deque([(src, 0)])   # (node, current min cost to this node)
        # do bfs
        while queue and stops <= k:
            # traverse nodes on the same graph level
            for _ in range(len(queue)):
                node, node_price = queue.popleft()
                # add next level nodes to the queue
                for node_dst, node_dst_price in graph[node]:
                    if node_price + node_dst_price >= min_prices[node_dst]:
                        continue
                    min_prices[node_dst] = node_price + node_dst_price
                    queue.append((node_dst, min_prices[node_dst]))

            stops += 1

        if min_prices[dst] != float('inf'):
            return min_prices[dst]
        else:
            return -1