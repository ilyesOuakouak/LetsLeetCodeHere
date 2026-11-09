class Solution(object):
    def partition(self, s):
        result = []
        path = []
    
        def recursion(start):
            if start == len(s):
                result.append(path[:])
                return
                
            for end in range(start, len(s)):
                if self.is_palindrom(s[start:end + 1]):
                    path.append(s[start:end + 1])
                    
                    recursion(end + 1)
                    path.pop()

            
        recursion(0)
        return result
    
    def is_palindrom(self, s):
        left = 0
        right = len(s) - 1
    
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
            
        return True
        