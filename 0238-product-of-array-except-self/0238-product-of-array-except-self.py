class Solution(object):
    def productExceptSelf(self, nums):
        
        size = len(nums)
        prefix = [1] * size

        for i in range(1, size):
            prefix[i] = prefix[i-1] * nums[i-1]

        suffix = 1
        for i in reversed(range(size)):
            current = nums[i]
            nums[i] = prefix[i] * suffix
            suffix *= current


        return nums 

       
        


        