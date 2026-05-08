class Solution(object):
    def letterCombinations(self, digits):
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if not digits:
            return []
        # 23

        queue = deque([""])
        result = []

        for digit in digits:
            size = len(queue)
            
            for _ in range(size):
                combination = queue.popleft() 
                for letter in mapping[digit]:
                    queue.append(combination + letter)
                
        
        return list(queue)




        

        