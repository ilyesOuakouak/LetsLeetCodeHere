class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        
        letters = {
            '2': "abc", 
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        result = []
        path = []

        if not digits:
            return []

        def backtrack(index):
            if index >= len(digits):
                result.append("".join(path))
                return 
            
            for letter in letters[digits[index]]:
                path.append(letter)
                backtrack(index + 1)
                path.pop()

        backtrack(0)

        return result



