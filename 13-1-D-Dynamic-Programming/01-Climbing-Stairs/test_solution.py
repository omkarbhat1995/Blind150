import pytest
from solution import Solution

sol = Solution()


@pytest.mark.parametrize("n, expected", [
    # --- Standard Examples ---
    (2, 2),                       # Example 1
    (3, 3),                       # Example 2

    # --- Minimum & Base Case Boundaries ---
    (1, 1),                       # Minimum constraint boundary (single step)
    (4, 5),                       # First non-trivial iterative step beyond examples
    (5, 8),                       # Small odd input

    # --- Small & Mid-Range Progression ---
    (6, 13),                      # Even progression
    (7, 21),                      # Odd progression
    (10, 89),                     # Double-digit milestone
    (12, 233),                    # Low triple-digit output
    (15, 987),                    # High triple-digit output

    # --- Exponential Growth (Catches Naive O(2^n) Recursion) ---
    (20, 10946),                  # Five-digit output
    (25, 121393),                 # Six-digit output
    (30, 1346269),                # Seven-digit output

    # --- Maximum Constraint Boundaries ---
    (44, 1134903170),             # Penultimate constraint boundary
    (45, 1836311903),             # Maximum constraint boundary (fits in 32-bit signed int)
])
def test_climbStairs(n, expected):
    """
    Tests the climbStairs method against 15 standard, boundary, and stress test cases.
    """
    assert sol.climbStairs(n) == expected