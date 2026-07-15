class Solution(object):
    def twoSum(self, numbers, target):
        # [2, 7, 11, 15] tar = 18

        left = 0 
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]


        return []

            
        