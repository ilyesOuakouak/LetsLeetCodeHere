from collections import deque
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        
        rows, cols = len(board), len(board[0])
        visited = set([])
        
        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))
            
            region = set([(r, c)])
            # FIX A: a yes/no flag, separate from the cells. Starts True if the start cell is on the edge.
            touches_edge = (r == 0 or c == 0 or r == rows - 1 or c == cols - 1)

            while queue:
                size = len(queue)
                    
                for _ in range(size):
                    r, c = queue.popleft()
                    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if nr < 0 or nc < 0 or nr >= rows or nc >= cols or board[nr][nc] == "X":
                            continue
                        
                        if nr == 0 or nc == 0 or nr == rows - 1 or nc == cols - 1:
                            touches_edge = True
                        
                        if (nr, nc) not in visited:
                            visited.add((nr, nc))
                            queue.append((nr, nc))
                            region.add((nr, nc))

            if not touches_edge:
                for r, c in region:
                    board[r][c] = "X"

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in visited:
                    bfs(r, c)
        

        
        














        