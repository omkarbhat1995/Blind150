class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Calculates x raised to the power of n using Binary Exponentiation.
        Achieves O(log n) time complexity.
        """
        # Base case for zero exponent
        if n == 0:
            return 1.0
        
        # Handle negative exponents by inverting the base
        if n < 0:
            x = 1 / x
            n = -n
            
        result = 1.0
        current_product = x
        
        while n > 0:
            # If the current power is odd, multiply the result by the current product
            if n % 2 == 1:
                result *= current_product
                
            # Square the base and halve the power for the next iteration
            current_product *= current_product
            n //= 2
            
        return result