import pytest
from solution import Solution

@pytest.mark.parametrize("n, expected", [
    # 1. Base Case: Zero
    (0, 0),
    
    # 2. Base Case: Single set bit at the beginning
    (1, 1),
    
    # 3. Standard LeetCode Example 1 (23 in decimal -> 10111 in binary)
    (23, 4),
    
    # 4. Standard LeetCode Example 2 (Max 32-bit signed minus 2)
    (2147483645, 30),
    
    # 5. Power of 2 (Only one 1-bit)
    (2, 1),
    
    # 6. Larger Power of 2
    (128, 1),
    
    # 7. Highest possible 32-bit signed integer (All 1s except sign bit)
    # Binary: 01111111111111111111111111111111
    (2147483647, 31),
    
    # 8. Highest possible 32-bit unsigned integer (All 32 bits are 1)
    # Binary: 11111111111111111111111111111111
    (4294967295, 32),
    
    # 9. Only the 32nd bit is set
    # Binary: 10000000000000000000000000000000
    (2147483648, 1),
    
    # 10. Alternating bits starting with 0
    # Binary: 01010101010101010101010101010101
    (1431655765, 16),
    
    # 11. Alternating bits starting with 1
    # Binary: 10101010101010101010101010101010
    (2863311530, 16),
    
    # 12. Small contiguous block of 1s (15 -> 1111)
    (15, 4),
    
    # 13. 8-bit max value (255 -> 11111111)
    (255, 8),
    
    # 14. 16-bit max value (65535 -> 16 ones)
    (65535, 16),
    
    # 15. Small arbitrary prime number (7 -> 111)
    (7, 3),
])
def test_hammingWeight(n, expected):
    """
    Tests the hammingWeight method against 15 bit-level edge cases.
    """
    sol = Solution()
    assert sol.hammingWeight(n) == expected