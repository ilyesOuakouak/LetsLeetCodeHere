class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        backets = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []
        if len(s) == 1:
            return False
            
        for c in s:
            
            if c in backets:
                stack.append(c)
            else:
                if stack:
                    poped_element = stack.pop()

                    if c != backets[poped_element]:
                        return False
                else: return False
                
        return not stack

# Here is a simplified version - great 

"""
stack = []
bracket_map = {')': '(', ']': '[', '}': '{'}

for char in s:
    if char in bracket_map:
        top = stack.pop() if stack else '#'

        if top != bracket_map[char]:
            return False
    else:
        stack.append(char)
return not stack
"""            
         
        