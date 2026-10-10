class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def build(current, opens, closes):
            if opens < n:
                build(current + "(", opens + 1, closes)
            if closes < opens:
                build(current + ")", opens, closes + 1)
            
            if opens == n and closes == n:
                result.append(current)

        build("", 0, 0)
        return result