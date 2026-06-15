class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [-2,1,-3,4,-1,2,1,-5,4]
        
        max_sum = float('-inf')
        current_sum = 0
        for num in nums:
            if current_sum < 0:
                current_sum = num
            else:   
                current_sum += num

            max_sum = current_sum if current_sum > max_sum else max_sum

        return max_sum

            
