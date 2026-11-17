from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Determines if the last index is reachable from index 0.
        Uses a Greedy algorithm working backwards: it continuously shifts 
        the target 'goal' closer to the start whenever a position can reach it.
        """
        goal = len(nums) - 1
        
        # Traverse backwards from the second-to-last element down to index 0
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
                
        return goal == 0