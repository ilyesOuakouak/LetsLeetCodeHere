class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        ways = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    ways[r][c] = 0
                elif r == 0 and c == 0:
                    ways[r][c] = 1
                
                else:
                    above = ways[r - 1][c] if r > 0 else 0
                    left = ways[r][c - 1] if c > 0 else 0
                    ways[r][c] = above + left

        return ways[m - 1][n - 1]