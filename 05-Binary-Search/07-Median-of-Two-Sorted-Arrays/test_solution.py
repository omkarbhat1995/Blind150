import unittest
from solution import Solution

class TestMedianSortedArrays(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_1_basic_odd(self):
        # Example 1
        self.assertEqual(self.sol.findMedianSortedArrays([1, 2], [3]), 2.0)

    def test_2_basic_even(self):
        # Example 2
        self.assertEqual(self.sol.findMedianSortedArrays([1, 3], [2, 4]), 2.5)

    def test_3_nums1_empty_odd(self):
        # One array is empty, result length is odd
        self.assertEqual(self.sol.findMedianSortedArrays([], [1, 2, 3]), 2.0)

    def test_4_nums1_empty_even(self):
        # One array is empty, result length is even
        self.assertEqual(self.sol.findMedianSortedArrays([], [1, 2, 3, 4]), 2.5)

    def test_5_single_elements(self):
        # Both arrays have exactly one element
        self.assertEqual(self.sol.findMedianSortedArrays([2], [3]), 2.5)

    def test_6_non_overlapping_smaller_first(self):
        # Arrays completely disjoint, smaller numbers in nums1
        self.assertEqual(self.sol.findMedianSortedArrays([1, 2, 3], [4, 5, 6]), 3.5)

    def test_7_non_overlapping_larger_first(self):
        # Arrays completely disjoint, larger numbers in nums1
        self.assertEqual(self.sol.findMedianSortedArrays([7, 8, 9], [1, 2, 3]), 5.0)

    def test_8_with_negatives(self):
        # Arrays containing negative numbers
        self.assertEqual(self.sol.findMedianSortedArrays([-5, -3, -1], [-4, -2, 0]), -2.5)

    def test_9_duplicates_and_same_elements(self):
        # Arrays with heavy duplicates
        self.assertEqual(self.sol.findMedianSortedArrays([1, 1, 1], [1, 1, 1, 1]), 1.0)

    def test_10_completely_inside(self):
        # One array's range is completely inside the other's
        self.assertEqual(self.sol.findMedianSortedArrays([4, 5, 6], [1, 2, 3, 7, 8, 9]), 5.0)

    def test_11_alternating_elements(self):
        # Elements naturally alternate
        self.assertEqual(self.sol.findMedianSortedArrays([1, 3, 5, 7], [2, 4, 6, 8]), 4.5)

    def test_12_very_large_numbers(self):
        # Upper bound constraint numbers
        self.assertEqual(self.sol.findMedianSortedArrays([1000000], [1000000]), 1000000.0)

    def test_13_large_arrays(self):
        # Simulate max constraints (m=1000, n=1000)
        nums1 = list(range(1, 1001))
        nums2 = list(range(1001, 2001))
        self.assertEqual(self.sol.findMedianSortedArrays(nums1, nums2), 1000.5)

    def test_14_one_element_vs_even_array(self):
        # Edge case balancing partitions heavily
        self.assertEqual(self.sol.findMedianSortedArrays([10], [1, 2, 3, 4, 5, 6]), 4.0)

    def test_15_one_element_vs_odd_array(self):
        # Edge case balancing partitions heavily
        self.assertEqual(self.sol.findMedianSortedArrays([1], [2, 3, 4, 5, 6]), 3.5)
        
    def test_16_zeroes(self):
        # Testing zeroes specifically
        self.assertEqual(self.sol.findMedianSortedArrays([0, 0], [0, 0]), 0.0)

if __name__ == '__main__':
    unittest.main()