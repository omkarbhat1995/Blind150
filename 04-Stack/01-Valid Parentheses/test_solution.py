import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("s, expected", [
    # Standard LeetCode Examples
    ("[]", True),                                 # Example 1
    ("([{}])", True),                             # Example 2
    ("[(])", False),                              # Example 3

    # Basic Valid Combinations
    ("()", True),                                 # Single pair
    ("()[]{}", True),                             # Adjacent pairs
    ("{[]}", True),                               # Nested pairs

    # Basic Invalid Combinations
    ("(]", False),                                # Mismatched types
    ("([)]", False),                              # Interleaved pairs
    ("((", False),                                # Missing closing brackets
    ("))", False),                                # Missing opening brackets

    # Extreme Edge Cases
    ("(", False),                                 # Length 1 boundary (Open)
    ("]", False),                                 # Length 1 boundary (Close)
    ("]()[", False),                              # Starts with close, ends with open
    
    # Large Scale / Boundary Tests
    ("(" * 500 + ")" * 500, True),                # Max constraint length (1000), fully valid nested
    ("(" * 500 + "]" + ")" * 499, False),         # Max constraint length, one wrong bracket in the middle
])
def test_isValid(s, expected):
    """
    Tests the isValid method against 15+ standard, boundary, and edge cases.
    """
    assert sol.isValid(s) == expected