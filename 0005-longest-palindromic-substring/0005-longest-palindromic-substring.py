class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Brute force is having a function isPalindrom, and check every possible string

        best = ""

        for i in range(len(s)):
            left = i
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            current_len = right - left - 1
            current_string = s[left + 1: right]

            best = current_string if len(current_string) > len(best) else best

            left = i - 1
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            current_len = right - left - 1
            current_string = s[left + 1: right]

            best = current_string if len(current_string) > len(best) else best

        return best 



        

