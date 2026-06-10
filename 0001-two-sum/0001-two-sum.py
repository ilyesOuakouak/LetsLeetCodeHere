class Solution:
    def twoSum(self, nums, target):   
        dic = {}
     

        for i in range(len(nums)):
            remaining = target - nums[i]

            if remaining in dic:
                return [i, dic[remaining]]
            
            if nums[i] not in dic:
                dic[nums[i]] = i
            
            
            
        return []






        


































"""
dic = {}

        for i in range(len(nums)):
            result = target - nums[i]
            if result in dic:
                return [i, dic[result]]
            
            dic[nums[i]] = i

        return []

"""