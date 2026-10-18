class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        original_count = {}

        for s in s1:
            original_count[s] = original_count.get(s, 0) + 1
    

        l = 0

        for r in range(len(s2)):
            c = s2[r]
            if c not in original_count:
                while l < r:
                    original_count[s2[l]] += 1 
                    l += 1
                l = r + 1  # skip c itself
                continue

            while original_count[c] == 0:
                original_count[s2[l]] += 1
                l += 1

            original_count[c] -= 1

            if r - l + 1 == len(s1):
                return True
        
        return False

                