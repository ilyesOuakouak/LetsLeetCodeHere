class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = {}
        result = []
        start = 0
        end = 0
        
        for i in range(len(s)):
            ch = s[i]
            last[ch] = i
        print(last)
        
            
        for i in range(len(s)):
            end = max(end, last[s[i]])
            if i == end:
                result.append(end - start + 1)
                start = i + 1

    
        return result