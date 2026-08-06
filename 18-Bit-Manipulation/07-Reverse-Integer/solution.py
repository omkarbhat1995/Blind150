class Solution:
    """
    Mathematical approach that strictly checks for 32-bit overflow 
    before it occurs.
    """
    def reverse(self, x: int) -> int:
        MAX_INT = 2147483647  # 2^31 - 1
        
        res = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        while x != 0:
            pop = x % 10
            x //= 10
            
            # Check for overflow before we apply the multiplier
            # If res > 214748364, then res * 10 will be > 2147483640 (Overflows)
            if res > MAX_INT // 10 or (res == MAX_INT // 10 and pop > 7):
                return 0
                
            res = (res * 10) + pop
            
        return res * sign