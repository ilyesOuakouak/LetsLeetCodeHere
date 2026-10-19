class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0])


        def dfs(r, c, visited):
            visited.add((r, c))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr >= 0 and nr < rows) and (nc >= 0 and nc < cols):
                    if (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, visited)

        
        pacific, atlantic = set(), set()

        for c in range(cols):
            dfs(0, c, pacific)
        for r in range(rows):
            dfs(r, 0, pacific)

        for c in range(cols):
            dfs(rows - 1, c, atlantic)
        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        return [[r, c] for (r, c) in pacific & atlantic]
        

