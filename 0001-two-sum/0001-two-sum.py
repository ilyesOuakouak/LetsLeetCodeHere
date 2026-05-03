class Solution:
    def twoSum(self, nums, target):   
        dic = {}

        for i in range(len(nums)):
            result = target - nums[i]
            if result in dic:
                return [i, dic[result]]
            
            dic[nums[i]] = i

        return []



        


