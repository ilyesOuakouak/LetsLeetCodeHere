class Solution:
    def combinationSum2(self, candidates, target):
        nums = sorted(candidates)
        result = []
        path = []

        def backtrack(start, remaining):
            if remaining == 0:       
                result.append(path[:])
                return                     

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue                   
                if nums[i] > remaining:
                    break                      

                path.append(nums[i])
                backtrack(i + 1, remaining - nums[i])
                path.pop()

        backtrack(0, target)
        
        return result