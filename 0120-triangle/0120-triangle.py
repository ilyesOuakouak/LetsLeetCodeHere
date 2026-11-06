class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = triangle[-1][:]
        
        for r in reversed(range(len(triangle) - 1)):
            for i in range(len(triangle[r])):
                dp[i] = triangle[r][i] + min(dp[i], dp[i + 1])
        return dp[0]
        
        
        
        """
        level = 1
     
        while level < len(triangle):
          
            nums = triangle[level]
            for i in range(len(nums)):
                if i == 0:
                    dp[level][i] = nums[i] + dp[level - 1][i]
                elif i == 1 and len(dp[level - 1]) == 1:
                    dp[level][i] = nums[i] + dp[level - 1][i - 1]
                elif i == 1 and len(dp[level - 1]) > 1:
                    dp[level][i] = nums[i] + min(dp[level - 1][i], dp[level - 1][i - 1])
                else:
                    if i >= len(dp[level - 1]):
                        dp[level][i] = nums[i] + dp[level - 1][i-1]
                    else:
                        dp[level][i] = nums[i] + min(dp[level - 1][i], dp[level - 1][i - 1])

            level += 1
            
            """