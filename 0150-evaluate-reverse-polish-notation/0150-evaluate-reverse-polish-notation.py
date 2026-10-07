class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        #operators = ['+', '-', '*', '/']
        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b),   
        }

        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                t1 = stack.pop()
                t2 = stack.pop()

                result = ops[token](t2, t1)
                stack.append(int(result))
        
        return stack[-1]
                
