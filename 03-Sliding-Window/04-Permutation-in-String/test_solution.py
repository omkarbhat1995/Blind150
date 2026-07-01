import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("s1, s2, expected", [
    # Provided Examples
    ("abc", "lecabee", True),           # Example 1
    ("abc", "lecaabee", False),         # Example 2
    
    # Classic LeetCode Edge Cases
    ("ab", "eidbaooo", True),           # Permutation in the middle
    ("ab", "eidboaoo", False),          # Characters are separated
    
    # Length Constraints
    ("a", "b", False),                  # Single characters, no match
    ("a", "a", True),                   # Single characters, match
    ("abc", "ab", False),               # s1 is longer than s2 (impossible)
    ("ab", "ab", True),                 # Exact match identical strings
    ("ab", "ba", True),                 # Exact match reversed strings
    
    # Prefix and Suffix Matches
    ("abc", "cbaxyz", True),            # Permutation at the absolute beginning
    ("abc", "xyzcab", True),            # Permutation at the absolute end
    
    # Frequency Traps
    ("hello", "ooolleoooleh", False),   # Similar characters, wrong frequencies
    ("adc", "dcda", True),              # Overlapping valid sub-components
    ("abb", "bba", True),               # Correct frequency duplicates
    ("abb", "bab", True),               # Scattered frequency duplicates
    
    # Extreme Boundaries
    ("a" * 1000, "a" * 1000, True),     # Max length constraint, exact match
    ("a" * 1000, "b" * 1000, False),    # Max length constraint, no match
    ("z" * 500, "a" * 500 + "z" * 500, True), # Massive prefix, valid match at the end
])
def test_checkInclusion(s1, s2, expected):
    """
    Tests the checkInclusion method against standard, constraint, and logical edge cases.
    """
    assert sol.checkInclusion(s1, s2) == expected