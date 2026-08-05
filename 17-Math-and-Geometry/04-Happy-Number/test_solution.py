import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("n, expected", [
    # Provided Examples
    (100, True),             # Example 1: Immediate 1 resolution
    (101, False),            # Example 2: Known cycle starting at 2

    # Minimum Boundary Constraints
    (1, True),               # Absolute minimum constraint, inherently non-cyclical
    (2, False),              # Standard small cycle trap

    # Standard Truthy Cases (Known Happy Numbers)
    (7, True),               # 7 -> 49 -> 97 -> 130 -> 10 -> 1
    (10, True),              # Simple base 10 reduction
    (13, True),              # 13 -> 10 -> 1
    (19, True),              # 19 -> 82 -> 68 -> 100 -> 1
    (23, True),              # 23 -> 13 -> 10 -> 1
    (68, True),              # Intermediate step of 19

    # Standard Falsy Cases (Known Unhappy/Cyclical Numbers)
    (3, False),              # Small cyclical
    (4, False),              # The core of the most common loop (4 -> 16 -> 37...)
    (20, False),             # Intermediate cyclical step

    # Maximum Boundary Constraints
    (999, False),            # Highest 3-digit number, expands to 243 -> 29 -> 85 -> 89 (Cycle)
    (1000, True),            # Maximum constraint limit, immediate 1 resolution
])
def test_isNonCyclical(n, expected):
    """
    Tests the isNonCyclical method against 15 standard, boundary, and edge cases.
    """
    assert sol.isNonCyclical(n) == expected