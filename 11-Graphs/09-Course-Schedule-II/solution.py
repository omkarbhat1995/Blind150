from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Finds a valid topological ordering of courses to finish all courses.
        Uses Kahn's Algorithm (BFS Topological Sort). Returns an empty list if a cycle is detected.
        """
        adj: List[List[int]] = [[] for _ in range(numCourses)]
        indegree: List[int] = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        # Start with all courses that have no prerequisites (in-degree of 0)
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order: List[int] = []

        while queue:
            curr = queue.popleft()
            order.append(curr)

            # Decrement the in-degree of all courses dependent on the completed course
            for dependent in adj[curr]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    queue.append(dependent)

        # If all courses are included in the ordering, the graph has no cycles
        return order if len(order) == numCourses else []