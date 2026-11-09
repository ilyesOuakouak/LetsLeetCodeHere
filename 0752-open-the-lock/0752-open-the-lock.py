class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        deadends = set(deadends)
        visited = set(["0000"])
        queue = deque(["0000"])
        level = 0

        while queue:
            for _ in range(len(queue)):
                current_code = queue.popleft()

                if current_code in deadends:
                    continue
                if current_code == target:
                    return level

                for nei in self.get_neighbours(current_code):
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            level += 1

        return -1

    def get_neighbours(self, code):
        result = []
        for i in reversed(range(4)):
            d = int(code[i])
            up = 0 if d == 9 else d + 1
            down = 9 if d == 0 else d - 1

            chars = list(code)
            chars[i] = str(up)
            result.append("".join(chars))

            chars[i] = str(down)
            result.append("".join(chars))
        return result
