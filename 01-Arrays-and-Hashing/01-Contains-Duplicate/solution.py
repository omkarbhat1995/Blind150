"""
Problem: Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/
Approach: Use a HashSet to track seen numbers. As we iterate, if a number is already in the set, a duplicate exists.
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False