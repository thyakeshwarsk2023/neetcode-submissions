class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course,prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        queue = deque([c for c in range(numCourses) if indegree[c]==0])
        completed = 0

        while queue:
            curr = queue.popleft()
            completed += 1

            for next_course in adj[curr]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        return completed == numCourses            

