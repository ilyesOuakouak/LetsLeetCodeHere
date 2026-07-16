class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0
        last_index = len(nums) - 1

        if last_index == 0:
            return True

        for i in range(last_index):
            if i > max_reach:
                return False

            max_reach = max(max_reach, i + nums[i])


            if max_reach >= last_index:
                return True
            
        
        return False

    
    """
    def canJump(self, nums):
    max_reach = 0
    last_index = len(nums) - 1

    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])

    return True
    """