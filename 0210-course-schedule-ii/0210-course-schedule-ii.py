class Solution:
    def findOrder(self, num_courses: int, prerequisites: list[list[int]]) -> list[int]:
        needs_me = defaultdict(list)
        remaining = [0] * num_courses
      
        order = []
        
        for u, v in prerequisites:
            needs_me[v].append(u)
            remaining[u] += 1       
            
        queue = deque()
        for course in range(num_courses):
            if remaining[course] == 0:
                queue.append(course)
            
        
        while queue:
            current_course = queue.popleft()
            order.append(current_course)
            
            for nxt in needs_me[current_course]:
                remaining[nxt] -= 1
                if remaining[nxt] == 0:
                    queue.append(nxt)
                    
        if len(order) < num_courses:
            return []
                
        
        return order