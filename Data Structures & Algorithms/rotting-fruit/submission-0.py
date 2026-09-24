from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        minutes = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r] [c] == 2:
                    queue.append((r,c))

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        while queue  and fresh > 0:
            length = len(queue)
            for i in range(length):
                r,c = queue.popleft()

                for dr,dc in directions:
                    nr = r + dr
                    nc = c+ dc

                    if(nr in range(len(grid))
                          and nc in range(len(grid[0]))
                          and grid[nr][nc] == 1
                          ):
                             grid[nr][nc] =2
                             queue.append((nr,nc))
                             fresh -= 1

            minutes+= 1
        return minutes if fresh == 0 else -1                     




