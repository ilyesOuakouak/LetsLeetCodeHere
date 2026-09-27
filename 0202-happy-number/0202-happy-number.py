class Solution(object):
    def isHappy(self, n):
        
        def square_digits(num):
            result = 0 
            while num > 0:
                last_d = num % 10
                result += last_d ** 2
                num = num // 10 

            return result

        seen = set()
        while n > 1:
            res = square_digits(n)
            if res in seen:
                return False
            seen.add(res)

            n = res
        
        return True


        



            
        