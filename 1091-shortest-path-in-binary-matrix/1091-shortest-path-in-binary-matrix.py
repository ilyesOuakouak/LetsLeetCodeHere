from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        """
            [
                [0,1],
                [1,0],
            ]
        """

        rows, cols = len(grid), len(grid[0])
        visited = set([(0, 0)])
        queue = deque([(0, 0)])
        round = 1

        if grid[0][0] != 0 or grid[rows - 1][cols - 1] != 0:
            return -1
        
        while queue:
            size = len(queue)

            for _ in range(size):
                r, c = queue.popleft()

                if r == (rows - 1) and c == (cols - 1):
                    return round

                
                directions = [(0, -1), (-1, 0), (0, 1), (1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 1:
                        continue
                    
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

                    
            round += 1
            
        return -1




