class Solution(object):
    def climbStairs(self, n):

        prev2 = 1 # ways to reach step 1
        prev1 = 2 # ways to reach step 2
        current = 2
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        for i in range(3, n + 1):
            current = prev2 + prev1
            prev2 = prev1
            prev1 = current
        
        return current
            
            







        