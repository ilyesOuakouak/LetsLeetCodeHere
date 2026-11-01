class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        subsets = []
        path = []
        result = []

        nums = sorted(candidates)

        def recursion(start):
            if sum(path) == target:
                subsets.append(path[:])
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                if nums[i] > target - sum(path):
                    return 
                    
                path.append(nums[i])
                recursion(i + 1)
                path.pop()
            
        recursion(0)

        return subsets