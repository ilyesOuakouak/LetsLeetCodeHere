class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # {1: 3, 2: 2, 3: 1} k = 2

        """{
            1: 4, 
            2: 3,
            3: 7,
            4: 1
        }"""

        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
    

        ordered = sorted(counts, key=counts.get, reverse=True)

        
        return ordered[:k]


        