class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        bi_graph = {}
        for preq_cor, cor in prerequisites:

            if preq_cor in bi_graph:
                bi_graph[preq_cor].add(cor)
            else:
                bi_graph[preq_cor] = set([cor])

        # Cache all reachable courses for each prerequisite we query.
        cache = {}
        res = []
        for preq_cor, cor in queries:
            if preq_cor not in cache:
                lst = list(bi_graph.get(preq_cor, set()))
                visited = set()

                while lst:
                    i = lst.pop()
                    if i in visited:
                        continue
                    visited.add(i)
                    lst.extend(bi_graph.get(i, set()))

                cache[preq_cor] = visited

            res.append(cor in cache[preq_cor])

        return res