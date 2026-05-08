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

        res = []

        
        def backtrack(index, path):
            # 1. Base Case: If the path is long enough...
            # Which means we reached a leaf 
            if index == len(digits):
                res.append(path)
                return 
            
            # get letter of the current digit 
            letters = mapping[digits[index]]

            for letter in letters:
                backtrack(index + 1, path + letter)


        


        # Start the recursion
        backtrack(0, "")
        return res





        """ This is a BFS solution 
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

        queue = deque([""]

        for digit in digits:
            size = len(queue)
            
            for _ in range(size):
                combination = queue.popleft() 
                for letter in mapping[digit]:
                    queue.append(combination + letter)
                
        
        return list(queue)

        """


        

        