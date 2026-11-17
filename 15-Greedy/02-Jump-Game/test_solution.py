import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("nums, expected", [
    # --- Standard LeetCode Examples ---
    ([1, 2, 0, 1, 0], True),                                       # Example 1: Valid path
    ([1, 2, 1, 0, 1], False),                                      # Example 2: Trapped at zero

    # --- Array Size Boundaries ---
    ([0], True),                                                   # Single element (already at target)
    ([1], True),                                                   # Single element, non-zero
    ([0, 1], False),                                               # Minimum invalid array (stuck at start)
    ([1, 0], True),                                                # Minimum valid jump to end

    # --- Zeros and Traps ---
    ([2, 0, 0], True),                                             # Exact jump over zeroes to the end
    ([3, 2, 1, 0, 4], False),                                      # Classic cascading trap leading to a zero
    ([1, 0, 1, 0], False),                                         # Stuck at the first zero
    ([1, 1, 1, 0], True),                                          # End is zero, which is perfectly valid

    # --- Large Jumps ---
    ([10, 1, 1, 1, 1, 1], True),                                   # Massive initial jump covers entire array
    ([2, 5, 0, 0, 0, 1, 0], True),                                 # Large jump from middle safely bypasses zeroes
    
    # --- Sequence Jumps ---
    ([1, 1, 1, 1, 1, 1, 1], True),                                 # Step-by-step strict traversal
    ([5, 4, 3, 2, 1, 0, 0], False),                                # Declining sequence ending in an inescapable trap
    
    # --- Maximum Constraints Simulator ---
    ([0] * 1000, False),                                           # Max size, all zeros (cannot move from index 0)
    ([1000] + [0] * 998 + [1], True),                              # Max size, massive jump clearing the entire board
])
def test_canJump(nums, expected):
    """
    Tests the canJump greedy algorithm against 15+ standard, boundary, and edge cases.
    """
    assert sol.canJump(nums) == expected