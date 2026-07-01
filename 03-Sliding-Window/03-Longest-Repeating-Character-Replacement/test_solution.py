import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("s, k, expected", [
    # Provided Examples
    ("XYYX", 2, 4),                     # Example 1
    ("AAABABB", 1, 5),                  # Example 2
    
    # Zero Replacements Allowed
    ("A", 0, 1),                        # Single character
    ("AB", 0, 1),                       # All unique, no replacements
    ("AABBC", 0, 2),                    # Small chunks, no replacements
    ("ABCDE", 0, 1),                    # Completely unique string
    
    # Generous Replacements Allowed
    ("ABAB", 2, 4),                     # k equals string length
    ("ABCDE", 5, 5),                    # k equals string length with all unique chars
    ("AABBCCDD", 4, 6),                 # Enough k to merge two large blocks
    
    # Internal Replacements (Bridging Gaps)
    ("AABBBBAA", 2, 6),                 # Can bridge the 'A's or modify the 'A's to 'B's
    ("ABBBACCCCA", 2, 6),               # Multiple dominant blocks competing
    ("KRSCDCSONAJNFAJAAJ", 4, 8),       # Random mix, multiple local maximums
    
    # Boundary Constraints
    ("A" * 1000, 0, 1000),              # Maximum length, all identical
    ("A" * 500 + "B" * 500, 500, 1000), # Maximum length, exactly enough k to make uniform
    
    # Alternating Strings
    ("ABABABAB", 1, 3),                 # Highly alternating, low k
    ("ABABABAB", 3, 7),                 # Highly alternating, medium k
])
def test_characterReplacement(s, k, expected):
    """
    Tests the characterReplacement method against 15+ standard, boundary, and edge cases.
    """
    assert sol.characterReplacement(s, k) == expected