class Solution(object):
    def reverse(self, x):
        negatif = False
        if x < 0:
            negatif = True
            x = abs(x)
        
        reversed_num = 0
        # 2^31 - 1 is 2147483647
        MAX_INT_BASE = 214748364  # The max number without its last digit

        while x > 0:
            digit = x % 10

            # 1. The Overflow Check (Before we do any math!)
            if reversed_num > MAX_INT_BASE or (reversed_num == MAX_INT_BASE and digit > 7):
                return 0

            reversed_num = (reversed_num * 10) + digit
            x = x // 10

        # Apply the negative sign back before checking the limits
        final_result = -reversed_num if negatif else reversed_num
    
        return final_result
        