class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """

        m = len(coins) + 1
        n = amount + 1
    
        rows, cols = m, n 

        grid = [ [0 for _ in range(cols)] for _ in range(rows)]

        grid[0][0] = 1

        for i in range(1, m):
            for a in range(n):
            
                skip = grid[i-1][a]
                use = grid[i][a - coins[i-1]] if a >= coins[i-1] else 0
                grid[i][a] = skip + use

        return grid[m-1][n-1]
        