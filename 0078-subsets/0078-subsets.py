class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        for num in reversed(nums):
            new_lists = [[num]]           # num alone
            for existing in result:
                new_lists.append([num] + existing)     # num in FRONT of existing
            result.extend(new_lists)

        result.append([])                 # the empty subset
        return result
            
            