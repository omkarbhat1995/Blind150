"""
Problem: Longest Consecutive Sequence
Link: https://leetcode.com/problems/longest-consecutive-sequence/
Approach: Hash Set. Convert array to a set. Iterate through the set, and only 
start counting a sequence if the current number has no left neighbor (num - 1). 
This ensures we only traverse sequences from their absolute start, achieving O(n) time.
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:
            # Check if this is the absolute start of a sequence
            length = 0
            if (n - 1) not in num_set:
                length = 1
                
                # Continuously check for the next consecutive elements
                while (n + length) in num_set:
                    length += 1
                    
                longest = max(longest, length)
                
        return longest