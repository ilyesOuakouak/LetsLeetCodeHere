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
                if count[char] < 0:
                    return False
                count[char] = count.get(char, 0) - 1
            else:
                return False


        return True


        
        
        

