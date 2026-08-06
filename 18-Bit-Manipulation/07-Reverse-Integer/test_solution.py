import pytest
from solution import Solution

@pytest.mark.parametrize("x, expected", [
    # 1. Standard LeetCode Example 1
    (123, 321),
    
    # 2. Standard LeetCode Example 2 (Negative number)
    (-123, -321),
    
    # 3. Standard LeetCode Example 3 (Overflows 32-bit limit)
    (120, 21),
    
    # 4. Input that causes an overflow upon reversing
    (1534236469, 0),
    
    # 5. Negative input that causes an overflow upon reversing
    (-1534236469, 0),
    
    # 6. Single digit positive
    (5, 5),
    
    # 7. Single digit negative
    (-9, -9),
    
    # 8. Zero
    (0, 0),
    
    # 9. Ends with multiple zeros
    (1200, 21),
    
    # 10. Negative ends with zero
    (-120, -21),
    
    # 11. Valid large input that just barely avoids overflow
    (1463847412, 2147483641),
    
    # 12. Valid negative large input that barely avoids overflow
    (-1463847412, -2147483641),
    
    # 13. Maximum 32-bit integer (Overflows when reversed)
    (2147483647, 0),
    
    # 14. Minimum 32-bit integer (Overflows when reversed)
    (-2147483648, 0),
    
    # 15. Palindrome
    (12321, 12321),
    
    # 16. Negative Palindrome
    (-12321, -12321),
])
def test_reverse(x, expected):
    """
    Tests the reverse method against limits, edge cases, and standard combinations.
    """
    sol = Solution()
    assert sol.reverse(x) == expected