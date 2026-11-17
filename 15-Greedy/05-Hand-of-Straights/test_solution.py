import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("hand, groupSize, expected", [
    # --- Standard LeetCode Examples ---
    ([1, 2, 4, 2, 3, 5, 3, 4], 4, True),                          # Example 1: Perfectly valid overlapping groups
    ([1, 2, 3, 3, 4, 5, 6, 7], 4, False),                         # Example 2: Invalid sequence generation

    # --- Array Size Constraints & Divisibility Boundaries ---
    ([1, 2, 3], 2, False),                                        # Length not divisible by groupSize
    ([1], 1, True),                                               # Absolute minimum constraint
    ([1, 2, 3, 4, 5], 5, True),                                   # Single maximum-sized group spanning entire array
    ([1, 2, 3, 4, 5], 1, True),                                   # groupSize of 1 is always valid

    # --- Duplicate & Gap Traps ---
    ([1, 1, 2, 2, 3, 3], 3, True),                                # Exact duplicate identical groups
    ([1, 2, 3, 5, 6, 7], 3, True),                                # Disjoint but valid separate sequences
    ([1, 2, 3, 5, 6], 5, False),                                  # Missing the mathematical link (4) to complete the set
    ([8, 10, 12], 3, False),                                      # Valid length, divisible, but elements aren't consecutive

    # --- Identical Value Rejections ---
    ([0, 0], 2, False),                                           # A group of 2 cannot contain identical values (must increment)
    ([10, 10, 10, 10], 2, False),                                 # Impossible to increment

    # --- Multi-Level Interlocking Sequences ---
    ([0, 1, 2, 3, 0, 1, 2, 3], 4, True),                          # Multiple sequences starting at zero
    ([10, 11, 12, 13, 11, 12, 13, 14], 4, True),                  # Staggered start sequences

    # --- Extreme Value Constraints ---
    ([1000, 1001, 1002, 1003], 4, True),                          # Maximum value constraints limit
    ([1, 2, 3, 4, 4, 5], 3, False),                               # Duplicate injected in the middle of an otherwise valid span
])
def test_isNStraightHand(hand, groupSize, expected):
    """
    Tests the isNStraightHand greedy algorithm against 16 standard, boundary, and edge cases.
    """
    assert sol.isNStraightHand(hand, groupSize) == expected