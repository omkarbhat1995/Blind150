import pytest
from solution import Solution

@pytest.mark.parametrize("n, expected", [
    # 1. Base Case: Zero (0000...0000 -> 0000...0000)
    (0, 0),
    
    # 2. Base Case: All 1s (1111...1111 -> 1111...1111)
    (4294967295, 4294967295),
    
    # 3. Only the 1st bit is set (000...0001 -> 100...0000)
    (1, 2147483648),
    
    # 4. Only the 32nd bit is set (100...0000 -> 000...0001)
    (2147483648, 1),
    
    # 5. Standard LeetCode Example 1 (21 -> 2818572288)
    (21, 2818572288),
    
    # 6. Standard LeetCode Example 2 (43261596 -> 964176192)
    (43261596, 964176192),
    
    # 7. Alternating bits starting with 1 (1010...1010 -> 0101...0101)
    (2863311530, 1431655765),
    
    # 8. Alternating bits starting with 0 (0101...0101 -> 1010...1010)
    (1431655765, 2863311530),
    
    # 9. Second bit set (000...0010 -> 010...0000)
    (2, 1073741824),
    
    # 10. Lower 16 bits are 1, upper 16 are 0 (65535 -> 4294901760)
    (65535, 4294901760),
    
    # 11. Upper 16 bits are 1, lower 16 are 0 (4294901760 -> 65535)
    (4294901760, 65535),
    
    # 12. Lower 8 bits are 1 (255 -> 4278190080)
    (255, 4278190080),
    
    # 13. Max 31-bit signed integer (All 1s except 32nd bit)
    (2147483647, 4294967294),
    
    # 14. Symmetric bits inside / Palindrome (Reverses to itself)
    (3221225475, 3221225475), # 11000000000000000000000000000011
    
    # 15. Arbitrary random number (123456789 -> 2830359264)
    (123456789, 2830359264),
])
def test_reverseBits(n, expected):
    """
    Tests the reverseBits method against 15 various bit-level edge cases and constraints.
    """
    sol = Solution()
    assert sol.reverseBits(n) == expected