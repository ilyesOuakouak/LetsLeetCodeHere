from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        visited = set([])

        def bfs(r, c):
            queue = deque([(r, c)])
            area = 0
            visited.add((r,c))

            while queue:
                size = len(queue)
                area += size

                for _ in range(size):
                    r, c = queue.popleft()
                    
                    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0:
                            continue

                        if (nr, nc) not in visited:
                            queue.append((nr, nc))
                            visited.add((nr, nc))
                           
            return area
                        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, bfs(r, c))
        
        return max_area
        

    def check(self, got, expected):
        if got == expected:
            print('OK')
        else:
            print('Not ok', [got, expected])


obj = Solution()

grid_1 = [[0,0,1,0], [0,0,0,0]]
grid_2 = [[0,0,1,0], [0,0,0,0], [1,1,1,1]]
grid_3 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
grid_4 = [[1]]
grid_5 = [[0]]
grid_6 = [[1,1], [1,1]]

find_area = obj.check(obj.maxAreaOfIsland(grid_1), 1)
find_area = obj.check(obj.maxAreaOfIsland(grid_2), 4)
find_area = obj.check(obj.maxAreaOfIsland(grid_3), 6)
find_area = obj.check(obj.maxAreaOfIsland(grid_4), 1)
find_area = obj.check(obj.maxAreaOfIsland(grid_5), 0)
find_area = obj.check(obj.maxAreaOfIsland(grid_6), 4)