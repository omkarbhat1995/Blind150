from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        rows = len(matrix)
        cols = len(matrix[0])
        
        left, right = 0, (rows * cols) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Map 1D index back to 2D coordinates
            row_val = mid // cols
            col_val = mid % cols
            
            mid_val = matrix[row_val][col_val]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False