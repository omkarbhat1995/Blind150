import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("nums, target, expected", [
    # Standard LeetCode Examples
    ([3, 4, 5, 6, 1, 2], 1, 4),                                 # Example 1: Target in right portion
    ([3, 5, 6, 0, 1, 2], 4, -1),                                # Example 2: Target missing

    # Boundary / Small Arrays
    ([1], 1, 0),                                                # Single element, target exists
    ([1], 0, -1),                                               # Single element, target missing
    ([2, 1], 1, 1),                                             # Two elements, rotated, target is 2nd
    ([2, 1], 2, 0),                                             # Two elements, rotated, target is 1st
    ([1, 2], 2, 1),                                             # Two elements, sorted

    # Unrotated (Fully Sorted) Array
    ([1, 2, 3, 4, 5, 6], 4, 3),                                 # Normal binary search behavior
    ([1, 2, 3, 4, 5, 6], 10, -1),                               # Normal missing

    # Target Exactly at Boundaries
    ([4, 5, 6, 7, 0, 1, 2], 4, 0),                              # Target is the absolute first element
    ([4, 5, 6, 7, 0, 1, 2], 2, 6),                              # Target is the absolute last element
    ([4, 5, 6, 7, 0, 1, 2], 7, 3),                              # Target is just before the pivot
    ([4, 5, 6, 7, 0, 1, 2], 0, 4),                              # Target is the pivot itself

    # Negative Numbers
    ([-2, -1, 0, 1, 2, -5, -4, -3], -4, 6),                     # Rotated negative numbers
    ([-5, -4, -3, -2, -1], -1, 4),                              # Sorted negative numbers
    
    # Missing Target Edge Cases
    ([4, 5, 6, 7, 8, 1, 2, 3], 10, -1),                         # Missing: larger than max
    ([4, 5, 6, 7, 8, 1, 2, 3], 0, -1),                          # Missing: smaller than min
    ([4, 5, 6, 8, 9, 1, 2, 3], 7, -1),                          # Missing: falls into a gap in the left sorted half
])
def test_search(nums, target, expected):
    """
    Tests the search method against 15+ standard, boundary, and edge cases,
    evaluating array parity, exact boundary indices, and missing item resolutions.
    """
    assert sol.search(nums, target) == expected