import pytest
from solution import Solution

@pytest.mark.parametrize("n, expected", [
    # 1. Base Case: Zero (Minimum constraint)
    (0, [0]),
    
    # 2. Minimum non-zero value
    (1, [0, 1]),
    
    # 3. Small sequence up to a power of 2
    (2, [0, 1, 1]),
    
    # 4. Standard LeetCode Example
    (4, [0, 1, 1, 2, 1]),
    
    # 5. Power of 2 (Only one 1-bit in the final number)
    (8, [0, 1, 1, 2, 1, 2, 2, 3, 1]),
    
    # 6. All 1s in binary (7 -> 111)
    (7, [0, 1, 1, 2, 1, 2, 2, 3]),
    
    # 7. Larger All 1s in binary (15 -> 1111)
    (15, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]),
    
    # 8. Another power of 2
    (16, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1]),
    
    # 9. Small arbitrary prime number
    (3, [0, 1, 1, 2]),
    
    # 10. Mid-range odd number
    (5, [0, 1, 1, 2, 1, 2]),
    
    # 11. Mid-range even number
    (10, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]),
    
    # 12. Larger power of 2
    (32, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 1]),
    
    # 13. Test case with just the final value directly verified to save visual space
    (127, [bin(i).count('1') for i in range(128)]),
    
    # 14. Mid-range boundary check
    (100, [bin(i).count('1') for i in range(101)]),
    
    # 15. Maximum constraint boundary (1000)
    (1000, [bin(i).count('1') for i in range(1001)]),
])
def test_countBits(n, expected):
    """
    Tests the countBits method against 15 various edge cases and constraints.
    """
    sol = Solution()
    assert sol.countBits(n) == expected