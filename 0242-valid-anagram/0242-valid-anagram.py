class Solution(object):
    def isAnagram(self, s, t):
        count = {}

        if len(t) != len(s):
            return False

        for char in s:
            count[char] = count.get(char, 0) + 1

        print(count)

        for char in t:
            if count.get(char):
                count[char] = count.get(char, 0) - 1
            else:
                return False


        return True


        
        
        

