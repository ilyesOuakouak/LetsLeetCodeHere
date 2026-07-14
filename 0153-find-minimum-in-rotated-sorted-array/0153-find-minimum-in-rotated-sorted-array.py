class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
            
        return nums[left]


"""
def dfs(left, right):
            if left == right: # when it remain only one index 
                return left

            mid = (left + right) // 2
            

            if nums[mid] > nums[right]:
                return dfs(mid + 1, right)

            else:
                return dfs(left, mid)


        return nums[dfs(0, len(nums) - 1)]

# check itterative ways below

""" 
"""
left = 0
    right = len(nums) - 1
    while left < right:      # Stop when they meet (left == right)
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid      # mid could be the min, so we keep it
    return nums[left]        # left is the answer
"""


""" 
left = 0
right = len(nums) - 1

while left <= right:
    mid = (right + left) // 2

    
    if nums[mid] < nums[right]:
        right = mid

    elif nums[mid] > nums[right]:
        left = mid + 1

    else: 
        return nums[mid]

"""

    

        

        