import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("piles, h, expected", [
    # Standard LeetCode Examples
    ([1, 4, 3, 2], 9, 2),                                          # Example 1
    ([25, 10, 23, 4], 4, 25),                                      # Example 2: h equals length of piles (must eat max pile)
    ([30, 11, 23, 4, 20], 5, 30),                                  # Example 3
    ([30, 11, 23, 4, 20], 6, 23),                                  # Just enough time to drop the rate slightly

    # Boundary Constraints (Smallest values)
    ([1], 1, 1),                                                   # Single pile, exactly 1 hour
    ([1], 10, 1),                                                  # Single pile, generous hours
    ([1, 1, 1, 1], 4, 1),                                          # All ones, h equals length
    
    # Uniform Piles
    ([10, 10, 10, 10], 4, 10),                                     # Uniform size, must eat 1 pile per hour
    ([10, 10, 10, 10], 40, 1),                                     # Extreme generous time, can eat 1 per hour

    # Extreme Constraints (Large values)
    ([1000000000], 2, 500000000),                                  # Max pile constraint, single pile
    ([1000000000, 1000000000], 2, 1000000000),                     # Max pile constraint, minimum h constraint
    ([1000000000, 1000000000], 3, 1000000000),                     # Odd hours with massive piles
    
    # Skewed Distribution
    ([1, 1, 1, 97], 100, 1),                                       # One massive pile, many tiny piles, huge hours
    ([1000, 1, 1, 1], 4, 1000),                                    # One massive pile, strict hours constraint
    
    # Mathematical Rounding Triggers
    ([3, 6, 7, 11], 8, 4),                                         # Forces math.ceil to evaluate varied remainders
    ([100, 100, 100], 100, 4)                                      # Very generous hours requiring a small speed rate (4 hours per pile mostly)
])
def test_minEatingSpeed(piles, h, expected):
    """
    Tests the minEatingSpeed method against 15+ standard, boundary, and extreme edge cases.
    Verifies optimal rate calculations, floating math ceilings, and bounds limits.
    """
    assert sol.minEatingSpeed(piles, h) == expected