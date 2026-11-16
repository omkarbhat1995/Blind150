from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Finds all unique subsets in an array containing duplicate numbers.
        Uses a two-choice backtracking decision tree (include/exclude) and 
        skips adjacent duplicates on the 'exclude' branch to prevent duplicate subsets naturally.
        """
        # Sorting is critical to group duplicates together so they can be skipped
        nums.sort()
        res = []

        def backtrack(i: int, current_subset: List[int]):
            # Base Case: Explored all numbers for the current path
            if i == len(nums):
                res.append(current_subset.copy())
                return
            
            # Decision 1: Include the current number
            current_subset.append(nums[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()
            
            # Decision 2: Exclude the current number
            # To prevent duplicate subsets, we must skip all identical numbers 
            # if we just chose to exclude the first instance of it.
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
                
            backtrack(i + 1, current_subset)

        backtrack(0, [])
        return res