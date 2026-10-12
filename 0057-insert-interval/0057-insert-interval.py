class Solution:
    def insert(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        
        n = len(intervals)
        result = []
        i = 0
        
        while i < n and intervals[i][1] < new_interval[0]:
            result.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= new_interval[1]:
            new_interval[0] = min(new_interval[0], intervals[i][0])
            new_interval[1] = max(new_interval[1], intervals[i][1])
            i += 1
        
        result.append(new_interval)

        while i < n and intervals[i][0] > new_interval[1]:
            result.append(intervals[i])
            i += 1

        return result 