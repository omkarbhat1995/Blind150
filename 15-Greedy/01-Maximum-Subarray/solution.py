from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Finds the contiguous subarray with the largest sum using Kadane's Algorithm.
        """
        max_sum = nums[0]
        current_sum = 0
        
        for num in nums:
            # If our running sum drops below zero, it becomes a liability. 
            # We reset it to zero to start a new potential subarray.
            if current_sum < 0:
                current_sum = 0
                
            current_sum += num
            max_sum = max(max_sum, current_sum)
            
        return max_sum