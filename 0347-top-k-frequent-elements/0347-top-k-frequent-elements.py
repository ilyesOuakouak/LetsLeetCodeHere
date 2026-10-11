class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # {1: 3, 2: 2, 3: 1} k = 2

        """{
            1: 4, 
            2: 3,
            3: 7,
            4: 1
        }"""

        n = len(nums)
        box = [[] for _ in range(n + 1)]
        result = []
        count_k = k

        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        print(counts)

        for key, val in counts.items():
            box[val].append(key)

        print(box)

        
        for i in reversed(range(len(box))):
            if count_k > 0:
                if box[i]:
                    for j in range(len(box[i])):
                        result.append(box[i][j])
                        count_k -= 1
            
                

        return result

        """
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
    
        ordered = sorted(counts, key=counts.get, reverse=True)
        
        return ordered[:k]
        """

        