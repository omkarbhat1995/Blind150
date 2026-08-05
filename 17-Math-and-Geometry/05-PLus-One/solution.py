from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Increments the large integer represented by the digits array by one.
        Handles carry-over by iterating in reverse.
        """
        # Iterate from the last digit to the first
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        
        # If we exit the loop, it means the number was entirely 9s (e.g., 999 -> 1000)
        return [1] + digits