import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("s, t, expected", [
    # Provided Examples
    ("OUZODYXAZV", "XYZ", "YXAZ"),             # Example 1
    ("xyz", "xyz", "xyz"),                     # Example 2
    ("x", "xy", ""),                           # Example 3
    
    # Classic LeetCode & Standard Cases
    ("ADOBECODEBANC", "ABC", "BANC"),          # Target dispersed across a long string
    ("a", "a", "a"),                           # Single character exact match
    ("ab", "b", "b"),                          # Target is at the very end
    ("ab", "a", "a"),                          # Target is at the very beginning
    
    # Multiple Matches (Finding the absolute minimum)
    ("bba", "ab", "ba"),                       # Two valid windows, shortest wins
    ("cabwefgewcwaefgcf", "cae", "cwae"),      # Multiple overlapping requirements
    ("aa", "a", "a"),                          # Duplicates in s, but only 1 needed from t
    
    # Duplicate Frequencies within target (t)
    ("aa", "aa", "aa"),                        # Target requires exactly two 'a's
    ("a", "aa", ""),                           # Target requires more duplicates than s contains
    ("abdaacbaa", "aba", "baa"),               # Complex frequency check
    
    # Case Sensitivity (Uppercase vs Lowercase)
    ("aA", "A", "A"),                          # Must match exact case
    ("A", "a", ""),                            # Wrong case, should return empty
    ("abBA", "bB", "bB"),                      # Mixed case valid window
    
    # Extreme Boundaries
    ("a" * 1000, "a" * 1000, "a" * 1000),      # Maximum string length constraints
    ("abcdefghijklmnopqrstuvwxyz", "a", "a"),  # Very long string, tiny one-character target
    ("abcdefghijklmnopqrstuvwxyz", "za", "abcdefghijklmnopqrstuvwxyz") # Target at absolute extremes
])
def test_minWindow(s, t, expected):
    """
    Tests the minWindow method against standard, constraint, and logical edge cases.
    """
    assert sol.minWindow(s, t) == expected