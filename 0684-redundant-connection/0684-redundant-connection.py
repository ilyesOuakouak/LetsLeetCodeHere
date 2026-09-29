class Solution(object):
    def findRedundantConnection(self, edges):
        # First we create a group for every node, 
        n = len(edges)
        parent = [i for i in range(n + 1)]  # everyone starts as their own leader 

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            parent[root_x] = root_y

        for a, b in edges:
            if find(a) == find(b):
                return [a, b]
            else:
                union(a, b)


            