class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        
        # 3 -> 2 -> 1 -> 0
        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)

        in_progress = set()
        visited = set()

        def dfs(node):
            if node in in_progress:
                return False
            
            if node in visited:
                return True
            
            in_progress.add(node)

            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False 
                
            in_progress.remove(node)
            visited.add(node)

            return True
            

        for course in range(numCourses):
            if not dfs(course):
                return False
            
        
        return True 


