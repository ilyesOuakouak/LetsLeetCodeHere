class Solution(object):
    def orangesRotting(self, grid):

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        # Step 1: one pass over the whole grid.
        # Every rotten orange -> add its (r, c) to the queue.
        # Every fresh orange -> count it (you'll need this for the -1 case).
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        minutes = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # Step 2: process the queue in rounds. One full pass = one minute.
        while queue and fresh_count > 0:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr >= 0 and nc >= 0 and nr < rows and nc < cols) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1

                        queue.append((nr, nc))

            minutes += 1

        return -1 if fresh_count > 0 else minutes  
    
