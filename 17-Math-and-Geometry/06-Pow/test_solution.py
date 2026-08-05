import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("x, n, expected", [
    # Provided Examples
    (2.00000, 5, 32.00000),             # Example 1: Standard positive power
    (1.10000, 10, 2.59374),             # Example 2: Fractional base
    (2.00000, -3, 0.12500),             # Example 3: Negative power

    # Base and Power Extremes (0 and 1)
    (10.00000, 0, 1.0),                 # Anything to the power of 0 is 1
    (0.00000, 5, 0.0),                  # 0 to any positive power is 0
    (1.00000, 1000, 1.0),               # 1 to any power is 1
    (5.00000, 1, 5.0),                  # Power of 1 returns the base

    # Negative Bases
    (-1.00000, 999, -1.0),              # Negative 1 to an odd power
    (-1.00000, 1000, 1.0),              # Negative 1 to an even power
    (-2.00000, 3, -8.0),                # Negative base, odd power
    (-2.00000, 4, 16.0),                # Negative base, even power

    # Fractional Bases with Negative Powers
    (2.50000, -2, 0.16000),             # Decimal base inverted and squared
    (-0.50000, -3, -8.0),               # Negative decimal, negative odd power

    # Constraint Boundaries
    (99.00000, 2, 9801.0),              # Upper bound base approximation
    (1.00001, 1000, 1.010049),          # Small fraction stress test
])
def test_myPow(x, n, expected):
    """
    Tests the myPow method against 15 standard, boundary, and edge cases.
    Utilizes pytest.approx to handle standard floating-point precision artifacts.
    """
    # rel=1e-5 provides a relative tolerance matching LeetCode's standard float acceptance
    assert sol.myPow(x, n) == pytest.approx(expected, rel=1e-5)