class Solution:

    def hours_needed(self, piles, k):
        total = 0
        for pile in piles:
            total += (pile + k - 1) // k

        return total

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        answer = max(piles)
        total = 0

        while left <= right:
            mid = (left + right) // 2

            # note that mid is k
            total = self.hours_needed(piles, mid)
            

            if total <= h:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
          
            
        
        return answer 

            
            
