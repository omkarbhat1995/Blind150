import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("temperatures, expected", [
    # Standard LeetCode Examples
    ([30, 38, 30, 36, 35, 40, 28], [1, 4, 1, 2, 1, 0, 0]),          # Example 1
    ([22, 21, 20], [0, 0, 0]),                                      # Example 2: Strictly decreasing

    # Basic Directional Arrays
    ([20, 21, 22], [1, 1, 0]),                                      # Strictly increasing
    ([30, 30, 30, 30], [0, 0, 0, 0]),                               # Plateau (all same)
    
    # Valleys and Mountains
    ([50, 40, 30, 20, 60], [4, 3, 2, 1, 0]),                        # Deep valley into a massive peak
    ([30, 40, 50, 40, 30], [1, 1, 0, 0, 0]),                        # Mountain peak in the middle
    ([90, 80, 70, 80, 90], [0, 3, 1, 1, 0]),                        # V-shape drop and return

    # Tricky Plateaus & Alternating Patterns
    ([1, 1, 1, 1, 2], [4, 3, 2, 1, 0]),                             # Long flat stretch followed by a bump
    ([80, 80, 80, 81], [3, 2, 1, 0]),                               # High plateau into a peak
    ([100, 1, 100, 1, 100], [0, 1, 0, 1, 0]),                       # Extreme alternating highs and lows

    # Extreme Constraints (Minimums and Maximums)
    ([1], [0]),                                                     # Length 1 boundary
    ([100, 100, 100], [0, 0, 0]),                                   # Maximum temp limit boundary
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]), # Continuous gentle climb

    # Large Scale Simulation (Constraints: length 1000)
    ([10] * 999 + [11], list(range(999, 0, -1)) + [0]),             # Max length: 999 days flat, 1 warmer day at end
    ([100] * 1000, [0] * 1000),                                     # Max length: completely flat max temp
])
def test_dailyTemperatures(temperatures, expected):
    """
    Tests the dailyTemperatures method against 15+ standard, boundary, and edge cases,
    focusing on directional changes, scale, and extreme plateaus.
    """
    assert sol.dailyTemperatures(temperatures) == expected