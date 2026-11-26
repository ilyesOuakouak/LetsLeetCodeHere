class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result = []
        path = []
        nums = sorted(nums)
        
        def recursion(index):
            result.append(path[:])
            
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                
                path.append(nums[i])
                
                recursion(i + 1)
                path.pop()
                
        
        recursion(0)
        
        return result