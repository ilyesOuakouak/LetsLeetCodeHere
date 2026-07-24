class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        if len(nums) == 1:
            return nums[0]

        global_max = nums[0]
        prev_max = nums[0]
        prev_min = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            temp_max = prev_max
            
            prev_max = max(num, num * prev_max, num * prev_min)
            prev_min = min(num, num * temp_max, num * prev_min)
            global_max = max(global_max, prev_max)
       

        return global_max


