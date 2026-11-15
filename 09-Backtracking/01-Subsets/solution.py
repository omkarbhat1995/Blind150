from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all possible subsets of the given array using backtracking.
        """
        res = []
        
        def backtracking(start: int, current_subset: List[int]):
            # Append a deep copy of the current subset to the result
            res.append(list(current_subset))

            # Explore further elements to add to the current subset
            for i in range(start, len(nums)):
                current_subset.append(nums[i])
                backtracking(i + 1, current_subset)
                current_subset.pop()
                
        backtracking(0, [])
        return res