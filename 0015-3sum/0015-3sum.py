class Solution:
    def threeSum(self, nums):
        # Time complexity is O(N2) because we have outer loop For and then the while loips,
        # This leads to O(n2)
        # For space we dont count the result array so it will be O(1) or we may consider O(N) 
        # because of sorting 
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                l = i + 1
                r = n - 1

                while l < r:
                    sum = nums[i] + nums[l] + nums[r]

                    if sum < 0:
                        l += 1
                    elif sum > 0:
                        r -= 1
                    else:
                        result.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
        return result

        """ res = []
        # TIME: O(N log N) - Sorting is fast, but not the bottleneck
        nums.sort()  # 1. Sort to enable Two Pointers logic
        
        n = len(nums)
        
        # TIME: This outer loop runs N times
        for i in range(n):
            # Optimization: If the current number is positive, we can't form 0 
            # because the array is sorted (all following numbers are also positive)
            if nums[i] > 0:
                break
                
            # DUPLICATE TRAP 1: Skip the same anchor number to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 2. Set up Two Pointers
            l, r = i + 1, n - 1
            
            # TIME: This inner while loop runs roughly N times for EACH 'i'
            # Total = N * N = O(N^2)
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    # Found a triplet!
                    res.append([nums[i], nums[l], nums[r]])
                    
                    # DUPLICATE TRAP 2: We need to move pointers AND skip duplicates
                    l += 1
                    r -= 1
                    
                    # Skip identical 'left' values
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                        
                    # (Optional optimization: skip identical 'right' values, 
                    # but just skipping left is enough to avoid duplicates)
                    
        return res """

            
