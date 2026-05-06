class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
            
        l = 0
        for r in range(1, len(nums)):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
                
        return l + 1
        
            

            

      
        





    

































