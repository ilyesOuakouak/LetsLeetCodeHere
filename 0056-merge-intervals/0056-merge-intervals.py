class Solution(object):
    def merge(self, intervals):
        # sorting with start 
        # [4, 7] [1, 4][3, 9] ==> [1, 4][3, 9][4, 7].  res = [[1, 4]]

        intervals.sort()
        resulted_arr = []
        resulted_arr.append(intervals[0])
 

        for i in range(1, len(intervals)):
            if intervals[i][0] <= resulted_arr[-1][1]:
                resulted_arr[-1][1] = max(resulted_arr[-1][1], intervals[i][1])
            else:
                resulted_arr.append(intervals[i])
           

        return resulted_arr




        

