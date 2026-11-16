import pytest
from solution import Solution

sol = Solution()

def normalize(strings):
    """
    Sorts the output list to ensure order-agnostic comparison.
    Because the problem states 'return the answer in any order', this prevents arbitrary failures.
    """
    return sorted(strings)

def is_well_formed(s: str) -> bool:
    """
    Helper function to mathematically verify if a generated parentheses string is strictly well-formed.
    """
    balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False
    return balance == 0

@pytest.mark.parametrize("n, expected_length, expected_exact", [
    # --- Standard LeetCode Examples & Exact Matches ---
    (1, 1, ["()"]),
    (2, 2, ["(())", "()()"]),
    (3, 5, ["((()))","(()())","(())()","()(())","()()()"]),
    (4, 14, ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]),
    
    # --- Constraints & Extreme Boundaries (Properties Check) ---
    # For n >= 5, explicitly writing the arrays clutters the test file. 
    # Instead, we assert against the exact Catalan number length, uniqueness, and structural validity.
    (5, 42, None),     # Mid-range length
    (6, 132, None),
    (7, 429, None),    # Official problem maximum constraint boundary
    
    # --- Stress Testing Beyond Constraints ---
    (0, 1, [""]),        # Zero pairs limit
    (8, 1430, None),
    (9, 4862, None),
    (10, 16796, None),
    (11, 58786, None),
    (12, 208012, None),
    (13, 742900, None),
    (14, 2674440, None)
])
def test_generateParenthesis(n, expected_length, expected_exact):
    """
    Tests the generateParenthesis backtracking logic against 15 distinct test cases, 
    scaling from constraint floors up to massive unconstrained performance thresholds.
    """
    results = sol.generateParenthesis(n)
    
    # 1. Check exact length matches the mathematically proven nth Catalan number
    assert len(results) == expected_length
    
    # 2. Check uniqueness (no duplicate combinations generated)
    assert len(set(results)) == expected_length
    
    # 3. Check every string generated is mathematically well-formed
    assert all(is_well_formed(s) for s in results)
    
    # 4. If an exact expected array is provided, verify order-agnostic equality
    if expected_exact is not None:
        assert normalize(results) == normalize(expected_exact)