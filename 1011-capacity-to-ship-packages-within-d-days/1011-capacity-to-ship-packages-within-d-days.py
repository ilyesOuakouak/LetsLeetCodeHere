class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        length = len(weights)
        
        low = max(weights)
        high = sum(weights)
        
        def can_ship(capacity):
            days_needed = 1
            load = 0
            
            for w in weights:
                if load + w > capacity:
                    days_needed += 1
                    load = 0
                load += w
                
            return days_needed <= days
                
        
        while low < high:
            capacity = (low + high) // 2
            
            if can_ship(capacity):
                high = capacity
            else:
                low = capacity + 1
        
        return low