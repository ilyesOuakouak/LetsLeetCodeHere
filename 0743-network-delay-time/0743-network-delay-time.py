class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        dic = defaultdict(list)
        
        best = {}
        heap = [(0, k)]
        
        for i in range(1, n + 1):
            if i != k:
                best[i] = float("inf")
            else:
                best[i] = 0
        
        print(best)
        
        for time in times:
            dic[time[0]].append((time[1], time[2]))
                        
        while heap:
            time, node = heapq.heappop(heap)
            
            if time > best[node]:
                continue
            
            for neighbourg, w in dic[node]:
                new_time = time + w
                
                if new_time < best[neighbourg]:
                    best[neighbourg] = new_time
                    heapq.heappush(heap, (new_time, neighbourg))
                    
        best_val = max(best.values())
        
        return best_val if  best_val != float('inf') else -1