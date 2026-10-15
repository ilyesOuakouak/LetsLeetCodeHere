from collections import deque
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
       

        rows, cols = len(matrix), len(matrix[0])
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []

        direction = deque(direction)
        r, c = 0, 0


        for _ in range(rows * cols):
            result.append(matrix[r][c])
            matrix[r][c] = "#"

            nr = r + direction[0][0]
            nc = c + direction[0][1]

            if nr < 0 or nc < 0 or nr >= rows or nc >= cols or matrix[nr][nc] == '#':
                direction.append(direction.popleft())
                nr = r + direction[0][0]
                nc = c + direction[0][1]

            r, c = nr, nc

        return result
