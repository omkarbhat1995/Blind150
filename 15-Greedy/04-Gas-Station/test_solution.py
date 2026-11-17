import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("gas, cost, expected", [
    # --- Standard LeetCode Examples ---
    ([1, 2, 3, 4], [2, 2, 4, 1], 3),                                 # Example 1: Valid circuit
    ([1, 2, 3], [2, 3, 2], -1),                                      # Example 2: Impossible circuit

    # --- Array Size Constraints (Length = 1) ---
    ([5], [4], 0),                                                   # Single station, valid
    ([4], [5], -1),                                                  # Single station, impossible
    ([2], [2], 0),                                                   # Single station, exact zero net gain

    # --- Zero Traps & Edge Cases ---
    ([0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 1], 0),                     # Mostly zeros, safe start at 0
    ([0, 0, 0, 2], [0, 0, 1, 0], 3),                                 # Debt incurs right before the payload
    ([3, 1, 1], [1, 2, 2], 0),                                       # Starting station carries the debt for the rest
    
    # --- Massive Jumps ---
    ([10, 0, 0, 0], [2, 2, 2, 2], 0),                                # Massive start covers all future travel
    ([0, 0, 0, 10], [2, 2, 2, 2], 3),                                # Massive end covers all accumulated travel wrapping around
    ([1, 1, 1, 1, 10], [2, 2, 2, 2, 2], 4),                          # Only the absolute last node can cover the previous debt

    # --- Permutations & Shifts ---
    ([2, 3, 4], [3, 4, 3], -1),                                      # Uniformly impossible
    ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),                           # Shifted successful start
    ([2, 3, 1], [3, 1, 2], 1),                                       # Standard wrap-around requirement

    # --- Exact Zero Sum Boundaries ---
    ([5, 1, 2, 3, 4], [4, 4, 1, 5, 1], 4),                           # Sum(gas) == Sum(cost), exactly
])
def test_canCompleteCircuit(gas, cost, expected):
    """
    Tests the greedy gas station algorithm against 15 distinct boundary, constraint, and edge cases.
    """
    assert sol.canCompleteCircuit(gas, cost) == expected
    