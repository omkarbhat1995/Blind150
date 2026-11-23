import pytest
from solution import Solution

sol = Solution()


@pytest.mark.parametrize("cost, expected", [
    # --- Standard Examples ---
    ([1, 2, 3], 2),                                        # Example 1
    ([1, 2, 1, 2, 1, 1, 1], 4),                            # Example 2
    ([10, 15, 20], 15),                                    # Classic LeetCode Example 1
    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),             # Classic LeetCode Example 2

    # --- Minimum Length Boundaries (length = 2) ---
    ([5, 10], 5),                                          # Start at index 0, jump 2
    ([10, 5], 5),                                          # Start at index 1, jump 1
    ([7, 7], 7),                                           # Equal costs

    # --- Uniform & Zero Cost Arrays ---
    ([0, 0, 0, 0, 0], 0),                                  # All zeros
    ([3, 3, 3, 3], 6),                                     # Identical non-zero, even length
    ([3, 3, 3, 3, 3], 6),                                  # Identical non-zero, odd length

    # --- Monotonic Sequences ---
    ([1, 2, 3, 4, 5, 6], 9),                               # Strictly increasing (0 -> 2 -> 4 -> top)
    ([6, 5, 4, 3, 2, 1], 9),                               # Strictly decreasing (1 -> 3 -> 5 -> top)

    # --- High-Cost Traps & Alternating Patterns ---
    ([0, 100, 0, 100, 0, 100], 0),                         # Skip every high-cost step completely
    ([100, 100, 0, 0, 100, 100], 200),                     # Forced to pay at start and end walls

    # --- Maximum Constraint Boundary ---
    ([100] * 100, 5000),                                   # Max length (100) and max value (100)
])
def test_minCostClimbingStairs(cost, expected):
    """
    Tests the minCostClimbingStairs method against 15 standard, boundary, and edge cases.
    """
    assert sol.minCostClimbingStairs(cost) == expected