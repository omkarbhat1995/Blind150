class Solution:
    """
    Optimal O(1) time and space solution using the n & (n - 1) bitwise trick 
    to continuously flip the least-significant 1-bit to 0.
    """
    def hammingWeight(self, n: int) -> int:
        count = 0
        
        while n:
            # Drops the lowest set 1-bit
            n &= (n - 1)
            count += 1
            
        return count