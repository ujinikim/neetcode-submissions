from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int
    ) -> int:
        graph = defaultdict(list)

        for start, end, price in flights:
            graph[start].append((end, price))

        heap = [(0, src, 0)]  # cost, node, edges_used
        best = {}

        while heap:
            cost, node, edges_used = heapq.heappop(heap)

            if node == dst:
                return cost

            if edges_used == k + 1:
                continue

            if (node, edges_used) in best and best[(node, edges_used)] < cost:
                continue

            best[(node, edges_used)] = cost

            for nei, price in graph[node]:
                heapq.heappush(heap, (cost + price, nei, edges_used + 1))

        return -1