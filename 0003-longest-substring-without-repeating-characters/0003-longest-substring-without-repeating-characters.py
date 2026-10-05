class Solution(object):
    def lengthOfLongestSubstring(self, s):

        # max_char = 0
        # ()
        max_char = 0
        seen = set()
        l = 0

        for r in range(len(s)):
        
            if s[r] not in seen:
                seen.add(s[r])
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])

            max_char = max(max_char, r - l + 1)

           
            
        print(len(seen))

        return max_char


