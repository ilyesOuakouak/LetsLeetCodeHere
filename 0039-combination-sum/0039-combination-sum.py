class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def build(current, left, start):
            if left == 0:
                result.append(current[:])
            elif left < 0:
                return 
            else:
                for i in range(start, len(candidates)):

                    current.append(candidates[i])
                    build(current, left - candidates[i], i)
                    current.pop()


        build([], target, 0)
        return result

    
    






