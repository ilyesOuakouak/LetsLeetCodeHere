class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True

            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False
            
            saved = board[r][c] # A
            board[r][c] = '#'
            found = True if dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1) else False

            board[r][c] = saved

            return found






        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
                
        return False


     
                
        









