import pytest
from solution import Solution

sol = Solution()

def normalize(combinations):
    """
    Sorts inner lists and the outer list to ensure order-agnostic comparison[cite: 2].
    Because the problem states 'return the combinations in any order', this prevents arbitrary failures[cite: 2].
    """
    return sorted([sorted(comb) for comb in combinations])

@pytest.mark.parametrize("candidates, target, expected", [
    # --- Standard LeetCode Examples ---
    ([10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]), # Example 1
    ([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]),                              # Example 2

    # --- Array Size Boundaries ---
    ([1], 1, [[1]]),                                                     # Single element, exact match
    ([1], 2, []),                                                        # Single element, no match

    # --- Duplicates & Frequencies ---
    ([2, 2, 2, 2, 2], 4, [[2, 2]]),                                      # All duplicates, target achievable
    ([2, 2, 2, 2, 2], 5, []),                                            # All duplicates, target impossible
    ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 3, [[1, 1, 1]]),                    # Extreme duplicates with small target

    # --- Value Variations & Combinations ---
    ([1, 2, 3, 4, 5], 15, [[1, 2, 3, 4, 5]]),                            # All elements needed
    ([1, 2, 3, 4, 5], 16, []),                                           # Exceeds sum of all elements
    ([2, 3, 6, 7], 7, [[7]]),                                            # Distinct elements, target exactly matches one

    # --- Target Constraints Boundaries ---
    ([5, 10, 15, 20], 30, [[10, 20], [5, 10, 15]]),                      # Multiples
    ([30, 30, 30], 30, [[30]]),                                          # Target exactly matches large constraints
    ([29, 1, 30], 30, [[1, 29], [30]]),                                  # Target bounds combinations

    # --- No Valid Combinations ---
    ([10, 20, 30], 5, []),                                               # Target smaller than any candidate
    ([4, 6, 8, 10], 11, []),                                             # Target unreachable with given parity

    # --- Distinct Subsets ---
    ([2, 3, 4, 5], 9, [[2, 3, 4], [4, 5]]),                              # Multiple valid non-overlapping branches
])
def test_combinationSum2(candidates, target, expected):
    """
    Tests the combinationSum2 method against 15 distinct boundary, edge, and standard cases.
    """
    assert normalize(sol.combinationSum2(candidates, target)) == normalize(expected)