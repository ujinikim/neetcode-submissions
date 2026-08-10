class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        visited = set()
        min_dist = [float("inf")] * n
        min_dist[0] = 0

        cost = 0

        for _ in range(n):
            curr = -1
            curr_dist = float("inf")

            # Pick cheapest unvisited point
            for i in range(n):
                if i not in visited and min_dist[i] < curr_dist:
                    curr = i
                    curr_dist = min_dist[i]

            visited.add(curr)
            cost += curr_dist

            # Update cost to reach every unvisited point
            for nei in range(n):
                if nei not in visited:
                    dist = (
                        abs(points[curr][0] - points[nei][0])
                        + abs(points[curr][1] - points[nei][1])
                    )

                    min_dist[nei] = min(min_dist[nei], dist)

        return cost