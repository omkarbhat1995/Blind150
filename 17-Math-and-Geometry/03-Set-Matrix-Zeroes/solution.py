from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Modifies the input matrix in-place to set rows and cols to 0
        if an element is 0. Achieves O(1) space complexity.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # Step 1: Mark the first row and first column
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        # Step 2: Use the marks to set inner matrix zeroes
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Step 3: Zero out the first column if needed
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # Step 4: Zero out the first row if needed
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0