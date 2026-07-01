import pytest
from solution import Solution

# Initialize the Solution object
sol = Solution()

@pytest.mark.parametrize("nums, expected", [
    # Standard LeetCode Examples
    ([1, 2, 3, 2, 2], 2),            # Example 1
    ([1, 2, 3, 4, 4], 4),            # Example 2
    
    # Duplicate Position Edge Cases
    ([2, 2, 1, 3], 2),               # Duplicate at the very beginning
    ([1, 3, 4, 2, 2], 2),            # Duplicate at the very end
    ([2, 1, 3, 2, 4], 2),            # Duplicates separated by other numbers
    
    # Frequency Edge Cases
    ([3, 3, 3, 3, 1], 3),            # The duplicate appears almost everywhere
    ([2, 2, 2, 2, 2, 2, 1], 2),      # High frequency variation
    ([1, 4, 4, 2, 3], 4),            # Exactly two duplicates in the middle
    
    # Boundary Constraints
    ([1, 1], 1),                     # Minimum possible constraint (n=1)
    ([1, 1, 2, 3, 4, 5], 1),         # Smallest possible number is the duplicate
    ([4, 3, 1, 4, 2], 4),            # Largest possible number is the duplicate
    
    # Simulated Larger Arrays
    ([5, 1, 2, 3, 4, 5], 5),         
    ([8, 7, 6, 5, 4, 3, 2, 1, 8], 8), 
    
    # Complex Cyclic Traps
    ([1, 3, 4, 2, 1], 1),            # Cycle returns directly to index 1
    ([2, 5, 9, 6, 9, 3, 8, 9, 7, 1], 9) # Scattered larger array with multi-repeats
])
def test_findDuplicate(nums, expected):
    """
    Tests the findDuplicate method against 15 standard, boundary, and edge cases.
    """
    assert sol.findDuplicate(nums) == expected