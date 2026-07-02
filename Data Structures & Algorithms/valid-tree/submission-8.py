class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        for e in edges:
            if e[0] > e[1]:
                e[0], e[1] = e[1], e[0]

        edges.sort()

        visited = [False] * n
        
        for i, e in enumerate(edges):
            if visited[e[1]] and visited[e[0]]:
                return False
            if not visited[e[1]] and not visited[e[0]]:
                if e[0] == e[1]:
                    return False
                if i != 0:
                    return False

            visited[e[1]] = True
            visited[e[0]] = True

        print(visited)

        return True

    # 01, 13, 23, 14