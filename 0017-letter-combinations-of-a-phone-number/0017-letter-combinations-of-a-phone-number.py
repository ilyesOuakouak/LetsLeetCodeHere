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

        results = [""]

        if not digits:
            return []

        for digit in digits:
            new_result = []
            for prefix in results:
                for letter in letters[digit]:
                    new_result.append(prefix + letter)
            results = new_result
        return results




