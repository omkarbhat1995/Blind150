import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("nums, expected", [
    # --- Standard LeetCode Examples ---
    ([2, -3, 4, -2, 2, 1, -1, 4], 8),                               # Example 1
    ([-1], -1),                                                     # Example 2
    ([5, 4, -1, 7, 8], 23),                                         # Classic continuous positive gain
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),                           # Classic mixed values (max is [4,-1,2,1])

    # --- Array Size Boundaries ---
    ([10000], 10000),                                               # Single element (max positive constraint)
    ([-10000], -10000),                                             # Single element (max negative constraint)
    ([0], 0),                                                       # Single element (zero)

    # --- Uniform Value Arrays ---
    ([1, 2, 3, 4, 5], 15),                                          # Strictly positive (take all)
    ([-5, -2, -9, -1, -3], -1),                                     # Strictly negative (must pick least negative single element)
    ([0, 0, 0, 0, 0], 0),                                           # Total zero array
    ([5, 5, 5, 5, 5], 25),                                          # Identical positive values

    # --- Value Fluctuations & Traps ---
    ([8, -19, 5, -4, 20], 21),                                      # Massive drop forces a reset, max is [5, -4, 20]
    ([2, -1, 2, -1, 2], 4),                                         # Small negative dips that are worth absorbing
    ([-5, 8, -5, 1, 1, -3, 5, -3], 8),                              # Max is a single peak, adjacent values drag it down
    ([10000, -10000, 10000, -10000], 10000),                        # Massive identical swings preventing growth
])
def test_maxSubArray(nums, expected):
    """
    Tests the maxSubArray algorithm across 15 distinct edge cases and permutations.
    """
    assert sol.maxSubArray(nums) == expected