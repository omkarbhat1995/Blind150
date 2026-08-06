from typing import List

class Solution:
    """
    Optimal O(n) time and O(1) space solution using Gauss's Formula.
    """
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Calculate the sum of numbers from 0 to n using Gauss's formula
        expected_sum = n * (n + 1) // 2
        
        # The missing number is the difference between the expected sum and actual sum
        actual_sum = sum(nums)
        
        return expected_sum - actual_sum

    def missingNumberXOR(self, nums: List[int]) -> int:
        """
        Alternative O(n) time and O(1) space solution using XOR.
        """
        n = len(nums)
        missing = n  # Start with n, as it is the only number not in the array
        
        for i in range(n):
            missing ^= i ^ nums[i]  # XOR all indices and values
        
        return missing