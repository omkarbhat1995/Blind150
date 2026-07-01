from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Finds the duplicate number in an array without modifying it
        and using O(1) extra space via Floyd's Cycle Detection.
        """
        # Phase 1: Find the intersection point of the two runners.
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
        # Phase 2: Find the "entrance" to the cycle.
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
            
        return slow