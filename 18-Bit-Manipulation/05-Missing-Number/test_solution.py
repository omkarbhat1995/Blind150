import pytest
from solution import Solution

# Extract the test cases into a variable so we can reuse them easily
TEST_CASES = [
    # 1. Standard LeetCode Example 1
    ([3, 0, 1], 2),
    
    # 2. Standard LeetCode Example 2 (Missing the last element)
    ([0, 1], 2),
    
    # 3. Standard LeetCode Example 3 (Missing the first element)
    ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    
    # 4. Smallest possible constraint (Missing 1)
    ([0], 1),
    
    # 5. Smallest possible constraint (Missing 0)
    ([1], 0),
    
    # 6. Sorted array missing the last element
    ([0, 1, 2, 3, 4], 5),
    
    # 7. Sorted array missing the first element
    ([1, 2, 3, 4, 5], 0),
    
    # 8. Sorted array missing a middle element
    ([0, 1, 2, 4, 5], 3),
    
    # 9. Unsorted array missing the last element
    ([2, 0, 1, 4, 3], 5),
    
    # 10. Unsorted array missing the first element
    ([4, 1, 2, 5, 3], 0),
    
    # 11. Scrambled larger array
    ([10, 8, 2, 0, 1, 4, 3, 9, 7, 5], 6),
    
    # 12. Reverse ordered array missing first sequence value
    ([3, 2, 1], 0),
    
    # 13. Reverse ordered array missing last sequence value
    ([2, 1, 0], 3),
    
    # 14. Larger dynamically generated test (Missing a middle value)
    ([x for x in range(101) if x != 50], 50),
    
    # 15. Max constraint simulation (Size 1000, missing 999)
    ([x for x in range(1001) if x != 999], 999),
]

@pytest.mark.parametrize("nums, expected", TEST_CASES)
def test_missingNumber(nums, expected):
    """
    Tests the missingNumber method (Gauss's formula) against 15 various edge cases.
    """
    sol = Solution()
    assert sol.missingNumber(nums) == expected

@pytest.mark.parametrize("nums, expected", TEST_CASES)
def test_missingNumberXOR(nums, expected):
    """
    Tests the missingNumberXOR method (Bit Manipulation) against 15 various edge cases.
    """
    sol = Solution()
    assert sol.missingNumberXOR(nums) == expected