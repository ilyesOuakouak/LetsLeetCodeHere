class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 1. Negative numbers are never palindromes (e.g., -121 != 121-)
        if x < 0:
            return False
        
        original = x  # Save original to compare later
        reversed_num = 0
        
        while x > 0:
            digit = x % 10          # Get last digit
            reversed_num = (reversed_num * 10) + digit # The Magic Formula
            x = x // 10             # Remove last digit
            
        return original == reversed_num
