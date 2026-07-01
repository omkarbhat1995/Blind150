import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("target, position, speed, expected", [
    # Standard LeetCode Examples
    (10, [1, 4], [3, 2], 1),                                        # Example 1
    (10, [4, 1, 0, 7], [2, 2, 1, 1], 3),                            # Example 2
    (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3),                     # Classic 5-car scenario
    
    # Boundary / Minimal Inputs
    (10, [3], [3], 1),                                              # Single car
    
    # Sequential States
    (10, [0, 1, 2, 3], [4, 3, 2, 1], 1),                            # Perfect cascading catch-up (all form 1 fleet)
    (10, [0, 1, 2, 3], [1, 2, 3, 4], 4),                            # Perfect spread (nobody catches up, 4 fleets)
    (20, [2, 4, 6, 8, 10], [5, 5, 5, 5, 5], 5),                     # Identical speeds, distinct fleets
    
    # Mathematical Precision / Edge Cases
    (10, [2, 4], [4, 3], 1),                                        # Exact same arrival time float match (2.0s)
    (10, [6, 8], [3, 2], 2),                                        # Close arrival times but no collision
    (10, [8, 6], [2, 4], 1),                                        # Fast car behind slow car, catches up quickly
    (100, [0, 2, 4], [4, 2, 1], 1),                                 # Multi-car catch-up far from target
    
    # Extreme Disparities
    (100, [10, 90], [100, 1], 1),                                   # Lightning-fast car catches crawling car perfectly
    (1000, [0, 999], [100, 1], 2),                                  # Fast car cannot catch up in time
    (1000, [10, 20, 30], [10, 10, 10], 3),                          # Spread evenly on a massive stretch
    
    # Long Distance Collisions
    (500, [100, 200, 300], [40, 20, 10], 1),                        # Large scale cascade
])
def test_carFleet(target, position, speed, expected):
    """
    Tests the carFleet method against 15 distinct boundary, precision, and state-change cases.
    """
    assert sol.carFleet(target, position, speed) == expected