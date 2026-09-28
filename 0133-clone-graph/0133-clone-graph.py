"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        if not node:                      # FIX 1: empty graph returns None (you    had this earlier; without it, deque([None]) crashes on node.val)
            return None

        dic = {}
        
        def manage(node):
            if node in dic:
                return dic[node]
            
            copy_node = Node(node.val)
            dic[node] = copy_node

            return copy_node
        
        first_node_copy = manage(node)    # FIX 2: save the starting copy once, before the loop
        queue = deque([node])

        while queue:
            node = queue.popleft()
            copy_node = manage(node)
            for n in node.neighbors:
                if n not in dic:
                    queue.append(n)
                copy_node.neighbors.append(manage(n)) # FIX 3: moved OUT of the if, so every edge is copied

        return first_node_copy
        

            


        

     
        
        
        