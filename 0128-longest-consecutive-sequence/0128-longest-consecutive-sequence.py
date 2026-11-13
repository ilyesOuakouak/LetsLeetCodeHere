class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        converted_set = set(nums)
        max_len = 0
        start = 0
        
        for num in converted_set:
            current = num
            
            if current - 1 in converted_set:
                continue
            
            start = current
            current_len = 0
            
            while start in converted_set:
                current_len += 1
                start += 1
                max_len = max(current_len, max_len)
        
            
        return max_len
        