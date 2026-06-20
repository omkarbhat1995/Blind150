import pytest
from solution import Solution

class TestContainsDuplicate:
    
    # Initialize the solution object once for the test class
    @pytest.fixture(autouse=True)
    def setup(self):
        self.solver = Solution()

    # Pytest decorator to cleanly pass multiple test cases
    @pytest.mark.parametrize("nums, expected", [
        # --- Standard LeetCode Examples ---
        ([1, 2, 3, 1], True),                                   # Basic duplicate
        ([1, 2, 3, 4], False),                                  # Basic no duplicate
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),                 # Multiple duplicates
        
        # --- Length Edge Cases ---
        ([], False),                                            # Empty array (Min length constraint)
        ([5], False),                                           # Single element
        ([1, 2], False),                                        # Two elements, no duplicate
        ([7, 7], True),                                         # Two elements, duplicate
        
        # --- Value Edge Cases (Constraints up to 10^9) ---
        ([10**9, 10**9], True),                                 # Max positive constraints
        ([-10**9, -10**9], True),                               # Min negative constraints
        ([10**9, -10**9, 10**5], False),                        # Mixed large numbers, no duplicate
        ([0, 0], True),                                         # Zeroes
        
        # --- Structural Edge Cases ---
        ([7, 7, 7, 7, 7, 7], True),                             # All identical elements
        ([1, 1, 2, 3, 4, 5, 6, 7], True),                       # Duplicate at the very beginning
        ([1, 2, 3, 4, 5, 6, 7, 7], True),                       # Duplicate at the very end
        ([1, -1, 2, -2, 3, -3, 1], True)                        # Alternating signs with a duplicate
    ])
    def test_containsDuplicate(self, nums, expected):
        assert self.solver.containsDuplicate(nums) == expected