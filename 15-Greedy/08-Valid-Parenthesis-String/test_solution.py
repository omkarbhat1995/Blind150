import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("s, expected", [
    # --- Standard LeetCode Examples ---
    ("((**)", True),                                     # Example 1
    ("(((*)", False),                                    # Example 2

    # --- Basic Exact Matches ---
    ("()", True),                                        # Simple valid pair
    ("(())", True),                                      # Nested valid pair
    (")(", False),                                       # Improper order

    # --- Wildcard Exact Replacements ---
    ("(*)", True),                                       # '*' as empty string
    ("(*))", True),                                      # '*' as '('
    ("((*)", True),                                      # '*' as ')'
    
    # --- Pure Wildcards ---
    ("*", True),                                         # Single wildcard (empty string)
    ("***", True),                                       # Multiple wildcards (empty string)

    # --- Leading and Trailing Edge Cases ---
    ("*)", True),                                        # Wildcard leading a close
    ("(*", True),                                        # Wildcard trailing an open
    ("*(", False),                                       # Wildcard leading an open (cannot resolve)
    (")*", False),                                       # Close leading a wildcard (instant fail)

    # --- Complex Interleaved Scenarios ---
    ("(*()**", True),                                    # Mixed wildcards closing and opening
    ("(((((*))))))", True),                             # Too many closing brackets for wildcards to save

    # --- Constraint Boundaries ---
    ("(" * 50 + "*" * 50, True),                         # 100 character max boundary (all wildcards act as closing)
    (")" * 50 + "*" * 50, False),                        # Instant fail at max boundary length
    ("(" * 100, False),                                  # All open, no closures
])
def test_checkValidString(s, expected):
    """
    Tests the checkValidString greedy algorithm across 15+ standard, boundary, and edge cases.
    """
    assert sol.checkValidString(s) == expected