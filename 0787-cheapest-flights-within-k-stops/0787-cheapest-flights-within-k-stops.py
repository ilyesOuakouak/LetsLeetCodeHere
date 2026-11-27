class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for _ in range(k + 1):
            new_prices = prices[:]     
            for start, end, cost in flights:
                if prices[start] != float('inf') and prices[start] + cost < new_prices[end]:
                    new_prices[end] = prices[start] + cost
                    
            prices = new_prices

        return prices[dst] if prices[dst] != float('inf') else -1 