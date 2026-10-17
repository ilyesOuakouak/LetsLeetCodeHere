class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        #indx:    0  1  2  3  4  5
        #nums:    0  1  0  3  2  3
        #best:    1  2  1  3  3  4

        best = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    best[i] = max(best[i], best[j] + 1)

        return max(best)




        



