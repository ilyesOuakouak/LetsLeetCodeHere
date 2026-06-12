class Solution(object):
    def isValid(self, s):
        brackets = { "(": ")", "[": "]", "{":"}" }
        stack = []

        for c in s:
            if c in brackets:
                stack.append(c)
        
            else:
                
                if not stack:
                    return False
                
                poped_char = stack.pop()
                if brackets[poped_char] != c:
                    return False

        return True if not stack else False




""" 
    dry-run
    stack = '[('

"""