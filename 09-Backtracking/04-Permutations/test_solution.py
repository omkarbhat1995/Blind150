import pytest
import itertools
from solution import Solution

sol = Solution()

def normalize(permutations):
    """
    Sorts the outer list of permutations to ensure order-agnostic comparison.
    Unlike combinations/subsets, we DO NOT sort the inner lists because 
    the distinct sequential order of the inner list is the mathematical definition of a permutation.
    """
    return sorted(permutations)

@pytest.mark.parametrize("nums, expected", [
    # --- Standard LeetCode Examples ---
    ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    ([7], [[7]]),

    # --- Array Size Boundaries ---
    ([10], [[10]]),                                                         # Single element (maximum constraint limit)
    ([-10], [[-10]]),                                                       # Single element (minimum constraint limit)
    ([0, 1], [[0, 1], [1, 0]]),                                             # Minimum multi-element array
    
    # --- Value Variations ---
    ([-1, -2, -3], list(map(list, itertools.permutations([-1, -2, -3])))),  # All negative values
    ([0, -1, 1], list(map(list, itertools.permutations([0, -1, 1])))),      # Negatives crossing zero
    ([4, 2, 6], list(map(list, itertools.permutations([4, 2, 6])))),        # Non-sequential positives
    ([-10, 10], [[-10, 10], [10, -10]]),                                    # Exact boundary extremes

    # --- Larger Scale Arrays (Automated Expected Generation) ---
    ([1, 2, 3, 4], list(map(list, itertools.permutations([1, 2, 3, 4])))),  # Length 4 (24 permutations)
    ([1, 2, 3, 4, 5], list(map(list, itertools.permutations([1, 2, 3, 4, 5])))), # Length 5 (120 permutations)
    
    # --- Maximum Constraints (Length = 6) ---
    # Python's itertools.permutations provides mathematical perfection for these 720-item assertions
    ([1, 2, 3, 4, 5, 6], list(map(list, itertools.permutations([1, 2, 3, 4, 5, 6])))),       # Max length, strictly increasing
    ([10, 9, 8, 7, 6, 5], list(map(list, itertools.permutations([10, 9, 8, 7, 6, 5])))),     # Max length, strictly decreasing
    ([-10, -8, -6, -4, -2, 0], list(map(list, itertools.permutations([-10, -8, -6, -4, -2, 0])))), # Max length, negative bounds
    
    # --- Unordered Jumbled Inputs ---
    ([3, 1, 4], list(map(list, itertools.permutations([3, 1, 4])))),        # Random standard unordered array
])
def test_permute(nums, expected):
    """
    Tests the permute method against 15 distinct boundary, edge, and standard cases.
    Leverages itertools.permutations dynamically for large arrays to keep the test file clean.
    """
    assert normalize(sol.permute(nums)) == normalize(expected)