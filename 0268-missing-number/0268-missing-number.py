class Solution(object):
    def missingNumber(self, nums):

        """
        array_nums = set()

        for num in nums:
            array_nums.add(num)
        
        for num in range(len(nums) + 1):
            if num not in array_nums:
                return num

        """

        result = 0

        for num in range(len(nums) + 1):
            result ^= num
        
        for num in nums:
            result ^= num

        return result
        