import pytest
from solution import Solution

@pytest.mark.parametrize("a, b, expected", [
    # 1. Standard LeetCode Example 1
    (1, 1, 2),
    
    # 2. Standard LeetCode Example 2
    (4, 7, 11),
    
    # 3. Both Zero
    (0, 0, 0),
    
    # 4. One Zero
    (5, 0, 5),
    
    # 5. The other Zero
    (0, 5, 5),
    
    # 6. Negative and Positive (canceling out)
    (-1, 1, 0),
    
    # 7. Both Negative
    (-5, -7, -12),
    
    # 8. Positive larger than Negative
    (10, -5, 5),
    
    # 9. Negative larger magnitude than Positive
    (-10, 5, -5),
    
    # 10. Larger Numbers
    (1000, 2000, 3000),
    
    # 11. Larger Negative Numbers
    (-1000, -2000, -3000),
    
    # 12. Negative and Positive Large
    (1000, -2000, -1000),
    
    # 13. Max 32-bit integer boundary addition
    (2147483647, 0, 2147483647),
    
    # 14. Min 32-bit integer boundary addition
    (-2147483648, 0, -2147483648),
    
    # 15. Negative base case causing quick carry
    (-1, -1, -2),
])
def test_getSum(a, b, expected):
    """
    Tests the getSum method against 15 various edge cases and boundaries.
    """
    sol = Solution()
    assert sol.getSum(a, b) == expected
