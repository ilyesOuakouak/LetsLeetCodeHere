class Solution:
    def rotate(self, grid: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(grid)
        
        for r in range(n // 2):
            for c in range(r, n - 1 - r):
                temp = grid[r][c]
                grid[r][c] = grid[n-1-c][r]
                grid[n-1-c][r] = grid[n-1-r][n-1-c]
                grid[n-1-r][n-1-c]= grid[c][n-1-r]
                grid[c][n-1-r] = temp
        
        