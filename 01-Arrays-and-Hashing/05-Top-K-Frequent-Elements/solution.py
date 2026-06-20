"""
Problem: Top K Frequent Elements
Link: https://leetcode.com/problems/top-k-frequent-elements/
Approach: Bucket Sort. Count frequencies, then group numbers into an array 
where the index is the frequency. Traverse the array backwards to get top k.
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each number
        count = Counter(nums)
        
        # Create an array of empty lists (buckets)
        # The index represents the frequency (0 to len(nums))
        freq = [[] for _ in range(len(nums) + 1)]
        
        # Populate the buckets: freq[frequency] = [num1, num2]
        for num, frequency in count.items():
            freq[frequency].append(num)
            
        res = []
        
        # Iterate backwards through the frequencies (from highest to lowest)
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                # Once we have found k elements, we can return immediately
                if len(res) == k:
                    return res
                    
        return res