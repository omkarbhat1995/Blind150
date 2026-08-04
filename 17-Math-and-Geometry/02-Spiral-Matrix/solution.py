from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Traverses an m x n matrix in spiral order using boundary pointers.
        Returns a 1D list of the matrix elements.
        """
        res = []
        if not matrix:
            return res
            
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        
        while left <= right and top <= bottom:
            # Traverse from left to right along the top boundary
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            
            # Traverse from top to bottom along the right boundary
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            
            # If boundaries cross, we've visited everything in this layer
            if not (left <= right and top <= bottom):
                break
                
            # Traverse from right to left along the bottom boundary
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            
            # Traverse from bottom to top along the left boundary
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            
        return res