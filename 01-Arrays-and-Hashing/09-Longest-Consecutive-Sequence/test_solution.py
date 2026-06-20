import pytest
from solution import Solution

class TestLongestConsecutive:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.solver = Solution()

    @pytest.mark.parametrize("nums, expected", [
        # --- Standard LeetCode Examples ---
        ([2, 20, 4, 10, 3, 4, 5], 4),
        ([0, 3, 2, 5, 4, 6, 1, 1], 7),
        ([100, 4, 200, 1, 3, 2], 4),
        
        # --- Length and Empty Edge Cases ---
        ([], 0),                                       # Empty array
        ([10], 1),                                     # Single element
        
        # --- Duplicates and Subsequences ---
        ([1, 2, 0, 1], 3),                             # Sequence with duplicates
        ([5, 5, 5, 5, 5], 1),                          # Only identical elements
        ([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], 7),      # Complex mixed arrays
        
        # --- Negative Values ---
        ([-5, -4, -3, -2, -1], 5),                     # Purely negative sequence
        ([1, -1, 0, 2], 4),                            # Crossing zero (-1, 0, 1, 2)
        
        # --- Gap Elements ---
        ([10, 20, 30, 40, 50], 1),                     # No consecutive elements at all
        
        # --- Extreme Value Constraints (-10^9 to 10^9) ---
        ([10**9, -10**9, 10**9 - 1, -10**9 + 1], 2)    # Min and max boundaries
    ])
    def test_longestConsecutive(self, nums, expected):
        assert self.solver.longestConsecutive(nums) == expected

    # --- Isolated Constraint Edge Cases ---
    
    def test_longestConsecutive_max_length_single_sequence(self):
        # Array of 1000 consecutive numbers in reverse order
        nums = [i for i in range(1000, 0, -1)]
        expected = 1000
        
        assert self.solver.longestConsecutive(nums) == expected

    def test_longestConsecutive_max_length_two_sequences(self):
        # Two sequences of length 500, spaced far apart
        seq1 = [i for i in range(1, 501)]
        seq2 = [i for i in range(10000, 10500)]
        nums = seq1 + seq2
        
        expected = 500
        assert self.solver.longestConsecutive(nums) == expected