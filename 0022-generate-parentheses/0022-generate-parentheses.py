class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        path = []
        
        
        def recursion(open, close):
            
            if len(path) == n * 2:
                result.append("".join(path))
                return  
            
            if open < n:
                path.append('(')
                recursion(open + 1, close)
                path.pop()
                
            if close < open:
                path.append(')')
                recursion(open, close + 1)
                path.pop()
            
        recursion(0 , 0)
        
        return result