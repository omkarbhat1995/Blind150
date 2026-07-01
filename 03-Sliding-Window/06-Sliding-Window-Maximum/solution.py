from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Finds the maximum element in a sliding window of size k at each step.
        
        :param nums: The array of integers.
        :param k: The size of the sliding window.
        :return: A list of the maximum elements from each window.
        """
        res = []
        q = deque()  # Stores indices, not values
        left = 0
        
        for right in range(len(nums)):
            # Remove smaller elements from the back of the deque as they are useless
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            
            q.append(right)
            
            # Remove the left value from the window if it's out of bounds
            if left > q[0]:
                q.popleft()
                
            # If our window has reached size k, append to results and shift the left pointer
            if (right + 1) >= k:
                res.append(nums[q[0]])
                left += 1
                
        return res