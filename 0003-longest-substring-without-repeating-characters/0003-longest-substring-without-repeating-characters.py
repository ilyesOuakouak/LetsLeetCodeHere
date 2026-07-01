class Solution(object):
    def lengthOfLongestSubstring(self, s):

        l = 0
        max_count = 0
        seen = set()
        
        for r in range(len(s)):
        
            current_char = s[r] # d

            if current_char not in seen:
                seen.add(current_char)     # (d v)
            else:
                while current_char in seen:
                    seen.remove(s[l])   
                    l += 1
                seen.add(current_char)

            current_count = r - l + 1 # 2
            max_count = max(max_count, current_count) # 2


        return max_count

            

            

            

