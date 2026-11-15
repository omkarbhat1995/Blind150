from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations in nums where the candidate numbers sum to target.
        Uses a two-choice backtracking decision tree to avoid duplicate combinations naturally.
        """
        res = []

        def backtrack(i: int, current_comb: List[int], current_sum: int):
            # Base Case 1: Target reached
            if current_sum == target:
                res.append(current_comb.copy())
                return
            
            # Base Case 2: Out of bounds or sum exceeded
            if i >= len(nums) or current_sum > target:
                return

            # Decision 1: Include the current candidate (stay on index 'i' to allow reuse)
            current_comb.append(nums[i])
            backtrack(i, current_comb, current_sum + nums[i])
            current_comb.pop()

            # Decision 2: Skip the current candidate (move to index 'i + 1')
            backtrack(i + 1, current_comb, current_sum)

        backtrack(0, [], 0)
        return res