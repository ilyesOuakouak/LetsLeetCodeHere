class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        dic = {}
        result = []

        for s in strs:
            my_tuple = [0] * 27
            for c in s:
                position = ord(c.lower()) - ord('a') + 1
                my_tuple[position] += 1
            
            key = tuple(my_tuple)
            
            if key not in dic:
                dic[key] = []
            dic[key].append(s)
            
                
        for key, val in dic.items():
            result.append(val)

        return result
            
            

        
        
            

                

        