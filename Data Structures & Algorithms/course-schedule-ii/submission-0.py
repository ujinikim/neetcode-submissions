from collections import deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        # prerequisite -> course
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        q = deque()

        # courses with no prerequisites
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        output = []

        while q:
            course = q.popleft()
            output.append(course)

            for nextCourse in adj[course]:
                indegree[nextCourse] -= 1

                if indegree[nextCourse] == 0:
                    q.append(nextCourse)

        # cycle exists if we couldn't finish every course
        if len(output) != numCourses:
            return []

        return output