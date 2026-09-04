class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        heap = [(0, k)]
        graph = defaultdict(list)
        res = 0

        for src, tg, t in times:
            graph[src].append((t, tg))

        while heap:
            t, node = heapq.heappop(heap)

            if node in visited:
                continue

            res = t
            visited.add(node)

            for n_time, n_node in graph[node]:
                heapq.heappush(heap, (n_time + t, n_node))

        return res if len(visited) == n else -1
            


