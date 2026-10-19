class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        test = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                piece = ""
                while stack and  stack[-1] != "[":
                    piece = stack.pop() + piece
                stack.pop() # pop this "["
                number = ""

                while stack and stack[-1].isdigit():
                    number = stack.pop() + number
                stack.append(piece * int(number))
                
        return "".join(stack)

        
        