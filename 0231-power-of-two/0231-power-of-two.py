class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # ln(n) / ln(2)

        if n <= 0: 
            return False
        
        while n > 1:
            if n % 2 != 0:
                return False
            n = n // 2
        
        return n == 1

        
