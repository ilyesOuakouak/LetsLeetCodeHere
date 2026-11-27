class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
       
        n = len(points)
        in_tree = [False] * n
        dist = [float('inf')] * n  
        dist[0] = 0
        total = 0

        for _ in range(n):
            u = min((d, i) for i, d in enumerate(dist) if not in_tree[i])[1]  
            in_tree[u] = True
            total += dist[u]
            for v in range(n):                                                  
                if not in_tree[v]:
                    d = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    dist[v] = min(dist[v], d)
        return total




