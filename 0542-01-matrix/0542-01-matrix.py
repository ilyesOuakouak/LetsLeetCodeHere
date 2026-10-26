class Solution:
    def updateMatrix(self, navigations: list[list[int]]) -> list[list[int]]:
        rows, cols = len(navigations), len(navigations[0])
        result = [[0] * cols for _ in range(rows)]
        queue = deque([])
        visited = set([])
        
        for r in range(rows):
            for c in range(cols):
                if navigations[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))


        while queue:
            size = len(queue)
            
            for _ in range(size):
                r, c = queue.popleft()
                
                directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                        continue
                        
                    if (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        result[nr][nc] = result[r][c] + 1 # great idea no need of distance variable 

        return result