import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("s, expected", [
    # Provided Examples
    ("zxyzxyz", 3),               # Example 1
    ("xxxx", 1),                  # Example 2
    
    # Standard Scenarios
    ("abcabcbb", 3),              # Classic example: "abc"
    ("pwwkew", 3),                # Answer is a substring ("wke"), not a subsequence ("pwke")
    ("abcdef", 6),                # All unique characters
    ("aab", 2),                   # Duplicate at the very beginning
    
    # Tricky Logical Edge Cases
    ("dvdf", 3),                  # Sliding window trap: jumping too far past 'd'
    ("abba", 2),                  # "abba" trap: ensure the left pointer doesn't move backwards
    
    # Whitespace & Special Character Edge Cases
    (" ", 1),                     # Single space
    ("   ", 1),                   # Multiple spaces
    (" !@#$%^&*", 9),             # Special characters, all unique including a space
    ("aA", 2),                    # Case sensitivity matters (printable ASCII)
    ("A1! A1!", 4),               # Mixed printable ASCII characters
    
    # Boundary Constraints
    ("", 0),                      # Length 0 constraint
    ("a", 1),                     # Length 1 constraint
    ("a" * 1000, 1),              # Maximum length constraint (1000 identical characters)
    ("ab" * 500, 2),              # Maximum length constraint (alternating characters)
])
def test_lengthOfLongestSubstring(s, expected):
    """
    Tests the lengthOfLongestSubstring method against standard, edge, and boundary cases.
    """
    assert sol.lengthOfLongestSubstring(s) == expected