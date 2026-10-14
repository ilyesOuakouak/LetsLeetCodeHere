class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = len(nums) -1
        l = 0
        p = 0

        """
                      l     r
            [0, 0, 0, 1, 1, 1, 2, 2, 2]
                           p
        """

        while p <= r:
            

            if nums[p] == 1:
                p += 1
            elif nums[p] == 0:
                nums[p], nums[l] = nums[l], nums[p]
                p += 1
                l += 1
            else:
                nums[p], nums[r] = nums[r], nums[p]
                r -= 1
    


        


        




        