from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Calculates the minimum number of jumps required to reach the last index.
        Uses a Greedy (implicit BFS) approach to track the maximum reachable 
        distance within the current jump window.
        """
        jumps = 0
        left = 0
        right = 0
        
        # We process until our current window reaches or surpasses the last index
        while right < len(nums) - 1:
            farthest = 0
            
            # Find the farthest index reachable from any position in our current window
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            
            # Move the window to the newly reachable territory
            left = right + 1
            right = farthest
            jumps += 1
            
        return jumps