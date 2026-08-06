class Solution:
    """
    Optimal O(1) time and space solution using bitwise shifting.
    """
    def reverseBits(self, n: int) -> int:
        res = 0
        
        # We must process exactly 32 bits
        for i in range(32):
            # Extract the rightmost bit of n
            bit = n & 1
            
            # Shift res to the left and append the extracted bit
            res = (res << 1) | bit
            
            # Shift n to the right to queue up the next bit
            n >>= 1
            
        return res