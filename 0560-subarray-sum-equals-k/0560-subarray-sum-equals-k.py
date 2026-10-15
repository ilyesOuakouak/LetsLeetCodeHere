class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        seen = {0: 1}

        total_prefix_sum = 0

        for i in range(len(nums)):
            total_prefix_sum += nums[i]

            if total_prefix_sum - k in seen:
                result += seen[total_prefix_sum - k]
                seen[total_prefix_sum] = seen.get(total_prefix_sum, 0) + 1
            else:
                seen[total_prefix_sum] = seen.get(total_prefix_sum, 0) + 1

        print(seen)
        return result


        
    
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(len(nums)):
            sum =nums[i]
            if sum == k:
                result += 1

            for j in range(i + 1, len(nums)):
                sum += nums[j]
                if sum == k:
                    result += 1
                    
                    
        return result
    """
    

