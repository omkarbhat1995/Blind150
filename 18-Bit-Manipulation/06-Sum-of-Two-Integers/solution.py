from typing import List

class Solution:
    """
    Optimal O(1) space and time solution using Bitwise Operations and 32-bit masking.
    """
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask in hexadecimal to simulate 32-bit integer boundaries
        mask = 0xFFFFFFFF
        
        # Iterate until there is no carry
        while b != 0:
            # a ^ b gives the sum without carry
            # (a & b) << 1 gives the carry
            # We apply the mask to handle negative numbers in Python's infinite precision
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
            
        # If 'a' represents a negative number in 32-bit (i.e., its MSB is 1)
        max_int = 0x7FFFFFFF
        if a <= max_int:
            return a
        else:
            # Convert back to Python's negative representation
            return ~(a ^ mask)
