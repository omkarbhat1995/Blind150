import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("s, expected", [
    # --- Standard LeetCode Examples ---
    ("xyxxyzbzbbisl", [5, 5, 1, 1, 1]),                                 # Example 1
    ("abcabc", [6]),                                                    # Example 2
    ("ababcbacadefegdehijhklij", [9, 7, 8]),                            # Classic LeetCode long example

    # --- Uniform & Unique Boundaries ---
    ("aaaaa", [5]),                                                     # All identical characters
    ("abcdef", [1, 1, 1, 1, 1, 1]),                                     # All unique characters
    ("z", [1]),                                                         # Single character minimum bound
    ("ab", [1, 1]),                                                     # Two distinct characters

    # --- Enveloping & Overlapping Patterns ---
    ("abccba", [6]),                                                    # 'a' wraps the entire string
    ("aaabccd", [3, 1, 2, 1]),                                          # Blocks of repeating characters
    ("abbacdde", [4, 1, 2, 1]),                                         # Symmetrical blocks disconnected
    ("abaca", [5]),                                                     # Zig-zagging occurrences tying it into one
    ("ababababab", [10]),                                               # Alternating dual characters

    # --- Maximum Size Constraints ---
    ("abcdefghijklmnopqrstuvwxyz", [1] * 26),                           # Complete alphabet unique list
    ("a" + "bcdefghijklmnopqrstuvwxy" + "a", [26]),                     # Complete alphabet engulfed by 'a' boundaries
    ("z" * 100, [100]),                                                 # Maximum length constraint bounds
])
def test_partitionLabels(s, expected):
    """
    Tests the partitionLabels greedy algorithm across 15 distinct boundary, constraint, and edge cases.
    """
    assert sol.partitionLabels(s) == expected