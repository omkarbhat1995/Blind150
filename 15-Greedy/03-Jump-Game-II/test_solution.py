import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("nums, expected", [
    # --- Standard LeetCode Examples ---
    ([2, 4, 1, 1, 1, 1], 2),                               # Example 1: Jump 0 -> 1 -> end
    ([2, 1, 2, 1, 0], 2),                                  # Example 2: Exact landing
    ([2, 3, 1, 1, 4], 2),                                  # Classic cascading greedy choice

    # --- Size Constraints & Boundaries ---
    ([0], 0),                                              # Single element (already at target)
    ([1], 0),                                              # Single element, non-zero
    ([1, 2], 1),                                           # Two elements, minimum valid jump
    ([1] * 1000, 999),                                     # Maximum size array, worst-case sequential jumps

    # --- Value Constraints & Massive Jumps ---
    ([100, 1, 1, 1, 1], 1),                                # Massive initial jump skips everything
    ([1, 1, 100, 1, 1], 3),                                # Massive jump in the middle
    ([5, 4, 3, 2, 1, 0], 1),                               # Declining sequence, one jump covers it all

    # --- Zero Traps (Guaranteed valid paths) ---
    ([3, 0, 0, 1], 1),                                     # Jump completely over zeros
    ([2, 1, 0], 1),                                        # Exactly lands on the zero at the end

    # --- Sequential & Step Patterns ---
    ([1, 1, 1, 1], 3),                                     # Forced one step at a time
    ([2, 2, 2, 2], 2),                                     # Even steps
    ([1, 2, 1, 1, 1], 3),                                  # Step-up then single steps
])
def test_jump(nums, expected):
    """
    Tests the jump greedy algorithm against 15 standard, boundary, and edge cases.
    """
    assert sol.jump(nums) == expected