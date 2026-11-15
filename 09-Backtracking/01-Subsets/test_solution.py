import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("nums, expected", [
    # --- Standard LeetCode Examples ---
    ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
    ([7], [[], [7]]),

    # --- Length Boundaries ---
    ([0], [[], [0]]),                                           # Single zero
    ([10], [[], [10]]),                                         # Single positive max constraint
    ([-10], [[], [-10]]),                                       # Single negative min constraint

    # --- Two Elements ---
    ([1, 2], [[], [1], [2], [1, 2]]),                           # Standard pairs
    ([-10, 10], [[], [-10], [10], [-10, 10]]),                  # Constraint boundary pairs
    ([-5, 5], [[], [-5], [5], [-5, 5]]),                        # Mixed signs

    # --- Three Elements ---
    ([-1, 0, 1], [[], [-1], [0], [1], [-1, 0], [-1, 1], [0, 1], [-1, 0, 1]]),   # Zero and mixed signs
    ([3, 2, 1], [[], [3], [2], [1], [3, 2], [3, 1], [2, 1], [3, 2, 1]]),        # Reversed sorted input
    ([-3, -2, -1], [[], [-3], [-2], [-1], [-3, -2], [-3, -1], [-2, -1], [-3, -2, -1]]), # All negatives
    ([-10, -9, -8], [[], [-10], [-9], [-8], [-10, -9], [-10, -8], [-9, -8], [-10, -9, -8]]),
    ([5, 10, -5], [[], [5], [10], [-5], [5, 10], [5, -5], [10, -5], [5, 10, -5]]),

    # --- Four Elements ---
    ([1, 2, 3, 4], [
        [], [1], [2], [3], [4], 
        [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4], 
        [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4], 
        [1, 2, 3, 4]
    ]),
    ([9, 10], [[], [9], [10], [9, 10]]),                        # Large positive pairs
])
def test_subsets(nums, expected):
    """
    Tests the subsets backtracking logic across 15 distinct boundary, edge, and standard cases.
    Because the problem allows subsets to be returned in ANY order, we must normalize the 
    result and expected arrays by sorting both the inner elements and the outer lists.
    """
    result = sol.subsets(nums)
    
    # 1. Sort the elements inside each subset (e.g., [2, 1] becomes [1, 2])
    normalized_result = [sorted(sub) for sub in result]
    normalized_expected = [sorted(sub) for sub in expected]
    
    # 2. Sort the outer list of subsets so they can be compared sequentially
    normalized_result.sort()
    normalized_expected.sort()
    
    assert normalized_result == normalized_expected