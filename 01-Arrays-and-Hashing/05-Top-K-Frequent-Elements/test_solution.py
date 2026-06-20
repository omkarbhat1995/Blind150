import pytest
from solution import Solution

class TestTopKFrequent:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.solver = Solution()

    @pytest.mark.parametrize("nums, k, expected", [
        # --- Standard LeetCode Examples ---
        ([1, 2, 2, 3, 3, 3], 2, [2, 3]),
        ([7, 7], 1, [7]),
        
        # --- Structural & Logic Edge Cases ---
        ([1, 1, 1, 2, 2, 3], 1, [1]),                                 # Top 1 only
        ([1, 1, 1, 2, 2, 3], 3, [1, 2, 3]),                           # Ask for all distinct elements
        ([5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 2, 2, 1], 3, [3, 4, 5]), # Strict frequency staircase
        ([4, 1, -1, 2, -1, 2, 3], 2, [-1, 2]),                        # Dispersed layout
        
        # --- Negative Values and Zeroes ---
        ([-1, -1, -2, -2, -2, -3], 2, [-1, -2]),                      # Negatives
        ([0, 0, 0, 1, 1, 2], 2, [0, 1]),                              # Zeroes
        ([-1000, -1000, 1000], 2, [-1000, 1000]),                     # Min/Max constraint values
        
        # --- Flat Distribution Constraints ---
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),                        # All distinct, k = all
        ([10, 10, 20, 20, 30, 30], 3, [10, 20, 30])                   # Ties handled by taking all (k=3)
    ])
    def test_topKFrequent(self, nums, k, expected):
        result = self.solver.topKFrequent(nums, k)
        
        # The problem states output can be in any order. 
        # We sort both lists to guarantee a deterministic comparison.
        assert sorted(result) == sorted(expected)

    # --- Isolated Constraint Edge Cases ---
    
    def test_topKFrequent_max_array_size_single_element(self):
        # Array of 10,000 identical elements
        nums = [500] * 10000
        k = 1
        expected = [500]
        
        result = self.solver.topKFrequent(nums, k)
        assert sorted(result) == sorted(expected)

    def test_topKFrequent_large_staircase(self):
        # Generates: [1, 2, 2, 3, 3, 3, ... 100 (x100)]
        nums = []
        for i in range(1, 101):
            nums.extend([i] * i)
            
        # Top 5 most frequent will be 100, 99, 98, 97, 96
        k = 5
        expected = [96, 97, 98, 99, 100]
        
        result = self.solver.topKFrequent(nums, k)
        assert sorted(result) == sorted(expected)