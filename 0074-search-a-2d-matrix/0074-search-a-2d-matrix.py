class Solution(object):
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
       
        left = 0
        right = m * n - 1
        

        while left <= right:
            mid = (left + right) // 2
            mid_row = mid // n
            mid_col = mid % n

            if target == matrix[mid_row][mid_col]:
                return True
            
            elif target > matrix[mid_row][mid_col]:
                left = mid + 1
            else:
                right = mid - 1
        
    
        return False
    






        