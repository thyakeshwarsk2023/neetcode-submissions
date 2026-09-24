class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            graph[course].append(pre)

        visited = set()
        path = set()
        order = []

        def dfs(course):
            if course in path:
                return False

            if course in visited:
                return True

            path.add(course)

            for pre in graph[course]:
                if not dfs(pre):
                    return False
            path.remove(course)
            visited.add(course)

            order.append(course)
            return True


        for course in range(numCourses):
            if not dfs(course):
                return []

        return order        



