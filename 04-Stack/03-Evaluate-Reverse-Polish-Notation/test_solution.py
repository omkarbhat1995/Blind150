import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("tokens, expected", [
    # Standard LeetCode Examples
    (["1", "2", "+", "3", "*", "4", "-"], 5),                                       # Example 1: ((1 + 2) * 3) - 4
    (["2", "1", "+", "3", "*"], 9),                                                 # Example 2
    (["4", "13", "5", "/", "+"], 6),                                                # Example 3
    (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),    # Example 4: Long expression

    # Boundary Length Constraints
    (["18"], 18),                                                                   # Single positive operand
    (["-18"], -18),                                                                 # Single negative operand
    
    # Division Truncation Edge Cases (Crucial for Python)
    (["-1", "2", "/"], 0),                                                          # Negative truncation toward zero
    (["1", "-2", "/"], 0),                                                          # Positive / Negative truncation
    (["5", "2", "/"], 2),                                                           # Standard positive truncation

    # Zero Involvements
    (["0", "3", "/"], 0),                                                           # Zero numerator
    (["0", "3", "*"], 0),                                                           # Multiplication by zero
    (["10", "0", "+", "5", "-"], 5),                                                # Addition with zero

    # Large Value / Extreme Constraint Limits
    (["-200", "-200", "*"], 40000),                                                 # Max negative values multiplied
    (["200", "200", "*", "40000", "-"], 0),                                         # Max positive limits balancing out
    
    # Sequential Chaining Operations
    (["2", "3", "*", "4", "5", "*", "+"], 26),                                      # (2 * 3) + (4 * 5)
    (["2", "2", "+", "2", "+", "2", "+"], 8),                                       # Repeated sequential addition
    (["10", "3", "/", "3", "*"], 9),                                                # Division resolution before multiplication
])
def test_evalRPN(tokens, expected):
    """
    Tests the evalRPN method against 15+ standard, boundary, and edge cases,
    with a specific focus on division truncation rules.
    """
    assert sol.evalRPN(tokens) == expected