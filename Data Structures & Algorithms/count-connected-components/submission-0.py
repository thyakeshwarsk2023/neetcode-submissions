class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i : [] for i in range(n)}

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)


        visited = set()

        def dfs(node):

            visited.add(node)

            for e in graph[node]:

                if e not in visited:
                    dfs(e)

        components = 0

        for i in range(n):
            if i not in  visited:
                dfs(i)

                components += 1
        return components                        


        