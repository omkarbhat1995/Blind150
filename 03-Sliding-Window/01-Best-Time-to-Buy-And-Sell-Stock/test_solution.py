import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("prices, expected", [
    # Standard Examples
    ([10, 1, 5, 6, 7, 1], 6),          # Provided Example 1
    ([10, 8, 7, 5, 2], 0),             # Provided Example 2 (Decreasing)
    ([7, 1, 5, 3, 6, 4], 5),           # Classic LeetCode example
    
    # Trend Edge Cases
    ([1, 2, 3, 4, 5, 6], 5),           # Strictly increasing prices
    ([5, 5, 5, 5, 5], 0),              # Stagnant prices, no profit
    
    # Trough and Peak Placements
    ([2, 4, 1], 2),                    # Lowest price is at the end, but best profit is earlier
    ([3, 2, 6, 5, 0, 3], 4),           # Profit before the absolute minimum
    ([2, 1, 2, 1, 0, 1, 2], 2),        # Multiple dips, finding max delta
    ([1, 100, 1, 100], 99),            # Volatile market, high variance
    
    # Boundary Constraints (Length & Values)
    ([10], 0),                         # Length 1 (can't buy and sell on different days)
    ([0, 100], 100),                   # Min boundary value to max boundary value
    ([100, 0], 0),                     # Max boundary value dropping to min boundary value
    ([0, 0], 0),                       # Minimum constraint bounds
    ([100, 100], 0),                   # Maximum constraint bounds
    
    # Large Arrays (Simulated)
    ([i for i in range(100, 0, -1)], 0), # 100 elements decreasing
    ([i for i in range(1, 101)], 99),    # 100 elements strictly increasing
])
def test_maxProfit(prices, expected):
    """
    Tests the maxProfit method against standard, trend, and boundary constraint edge cases.
    """
    assert sol.maxProfit(prices) == expected