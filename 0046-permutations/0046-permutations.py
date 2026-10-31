class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        path = []
        
        def recursion():
  
            if len(path) == len(nums):
                result.append(path[:])
            
            for i in range(len(nums)):
                
                if not nums[i] in path:
                    path.append(nums[i])                              
                    recursion()
                    path.pop()
                else:
                    continue
                    
            
 
        recursion()
        
        return result