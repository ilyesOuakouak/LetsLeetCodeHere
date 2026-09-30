class Solution(object):
    def findPeakElement(self, nums):
    
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left
            

        """
        left = 0
        right = len(nums) -1 #

        if len(nums) == 1:
            return 0
        
        
        while left <= right:
            mid = (left + right) // 2 #left + (right - left) // 2
        
            if mid == 0:
                if nums[mid] > nums[mid + 1]:
                    return mid
                
                elif nums[mid] < nums[mid + 1]:
                    left += 1

                else:
                    right -= 1

            elif mid == len(nums) - 1:
                if nums[mid - 1] < nums[mid]:
                    return mid

                elif nums[mid] < nums[mid + 1]:
                    left += 1

                
                else:
                    right -= 1

            else:
                if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                    return mid

                elif nums[mid] < nums[mid + 1]:
                    left += 1

                
                else:
                    right -= 1

        return 0
        """

        