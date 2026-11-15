import pytest
from solution import Solution

sol = Solution()

def normalize(combinations):
    """
    Sorts inner lists and the outer list to ensure order-agnostic comparison[cite: 2].
    Because the problem states 'return the combinations in any order', this prevents arbitrary failures[cite: 2].
    """
    return sorted([sorted(comb) for comb in combinations])

@pytest.mark.parametrize("nums, target, expected", [
    # --- Standard LeetCode Examples ---
    ([2, 5, 6, 9], 9, [[2, 2, 5], [9]]),                                                # Example 1
    ([3, 4, 5], 16, [[3, 3, 3, 3, 4], [3, 3, 5, 5], [4, 4, 4, 4], [3, 4, 4, 5]]),       # Example 2
    ([3], 5, []),                                                                       # Example 3

    # --- Array Size Boundaries ---
    ([3], 9, [[3, 3, 3]]),                                                              # Single element, perfectly divisible
    ([3], 5, []),                                                                       # Single element, impossible

    # --- Value Variations ---
    ([2, 4, 6, 8], 10, [[2, 2, 2, 2, 2], [2, 2, 2, 4], [2, 2, 6], [2, 4, 4], [2, 8], [4, 6]]), # Evens
    ([1, 2, 3], 4, [[1, 1, 1, 1], [1, 1, 2], [1, 3], [2, 2]]),                          # Small numbers, numerous combinations
    ([7, 3, 2], 5, [[2, 3]]),                                                           # Unordered candidates

    # --- Target Constraints Boundaries ---
    ([2, 3, 4], 2, [[2]]),                                                              # Target exactly equals the minimum candidate
    ([5, 10, 15], 30, [[5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 10], [5, 5, 10, 10], [5, 10, 15], [5, 5, 5, 15], [10, 10, 10], [15, 15]]), # Multiples

    # --- No Valid Combinations ---
    ([5, 10, 15], 4, []),                                                               # Target smaller than any candidate
    ([4, 6, 8], 11, []),                                                                # Target unreachable with even constraint
    ([10, 20], 15, []),                                                                 # Target unreachable with large minimums

    # --- Large Single-Step Jumps ---
    ([20, 30], 30, [[30]]),                                                             # Target exactly matches one large candidate
    ([3, 4, 5], 11, [[3, 4, 4], [3, 3, 5]]),                                            # Interlocking mid-sized steps
])
def test_combinationSum(nums, target, expected):
    """
    Tests the combinationSum method against 15 distinct boundary, edge, and standard cases.
    """
    assert normalize(sol.combinationSum(nums, target)) == normalize(expected)