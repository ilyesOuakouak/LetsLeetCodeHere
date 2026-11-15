class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        max_heap = []
        result = []
        
        for i in range(k):
            distance = self.get_distance(points[i])
            heapq.heappush(max_heap, (-distance, points[i]))
            
        for i in range(k, len(points)):
            current_distance = -self.get_distance(points[i])
            d, popped_point = max_heap[0]
            
            if current_distance > d:
                popped = heapq.heappop(max_heap)
                heapq.heappush(max_heap, (current_distance, points[i]))
            
        for _ in range(k):
            distance, popped = heapq.heappop(max_heap)
            result.append(popped)
            
        return result
    
    def get_distance(self, point: list):
        return point[0]**2 + point[1]**2