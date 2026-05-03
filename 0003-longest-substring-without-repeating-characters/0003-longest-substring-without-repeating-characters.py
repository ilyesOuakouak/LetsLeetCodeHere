class Solution(object):
    def lengthOfLongestSubstring(self, s):

        left = 0
        visited = set()
        max_len = 0

        for right in range(len(s)):
            # 1. If s[right] is already in visited, we MUST shrink from the left
            # until s[right] is removed.
            while s[right] in visited:
                visited.remove(s[left])
                left += 1
            
            visited.add(s[right])
   
            
            # Update max_len (The window [left...right] is now valid!)
            max_len = max(max_len, (right - left) + 1)
            
        return max_len




