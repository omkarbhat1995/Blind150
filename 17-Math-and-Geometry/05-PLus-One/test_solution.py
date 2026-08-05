import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("digits, expected", [
    # Provided Examples
    ([1, 2, 3, 4], [1, 2, 3, 5]),      # Example 1: Standard no-carry
    ([9, 9, 9], [1, 0, 0, 0]),         # Example 2: All nines, array expands

    # Single Digit Constraints
    ([0], [1]),                        # Absolute minimum edge case
    ([9], [1, 0]),                     # Single nine expansion

    # Isolated Carry-Overs
    ([1, 9], [2, 0]),                  # Carry over at the very end
    ([2, 9, 9], [3, 0, 0]),            # Multiple carry-overs stopping before index 0
    ([1, 0, 9], [1, 1, 0]),            # Carry over isolating in the middle
    ([8, 9, 9, 9], [9, 0, 0, 0]),      # Massive carry stopping just at the start

    # Standard Variations
    ([4, 3, 2, 1], [4, 3, 2, 2]),      # Standard descending digits
    ([1, 0, 0, 0], [1, 0, 0, 1]),      # Lots of interior zeroes
    ([9, 8, 7, 6], [9, 8, 7, 7]),      # Number starts with 9 but no carry reaches it
    ([8, 9, 8, 9], [8, 9, 9, 0]),      # Alternating 9s, isolating the carry
    ([1, 9, 9, 0], [1, 9, 9, 1]),      # 9s in the array but the last digit is standard
    ([5, 5, 5, 5], [5, 5, 5, 6]),      # All identical non-nine elements

    # Maximum Boundary Constraints
    ([9] * 100, [1] + [0] * 100),      # Max length array full of 9s
])
def test_plusOne(digits, expected):
    """
    Tests the plusOne method against 15 standard, boundary, and edge cases.
    """
    # Create a fresh copy to avoid in-place mutation side effects during Pytest parameterization
    input_digits = digits.copy()
    assert sol.plusOne(input_digits) == expected