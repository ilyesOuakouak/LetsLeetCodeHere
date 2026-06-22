class Solution(object):
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        print(dp)

        for case in range(1, len(dp)):
            for coin in coins:
                if case - coin >= 0:
                    dp[case] = min(dp[case], 1 + dp[case - coin])
        

        return  dp[amount] if dp[amount] != float('inf') else -1

    




