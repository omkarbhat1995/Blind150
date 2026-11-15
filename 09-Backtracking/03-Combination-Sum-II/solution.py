from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations in candidates that sum to target.
        Each number in candidates may only be used once in the combination.
        """
        # Sorting is crucial to group duplicates and enable early termination pruning
        candidates.sort()
        res = []

        def backtrack(start: int, current_comb: List[int], current_sum: int):
            # Base Case 1: Target reached
            if current_sum == target:
                res.append(current_comb.copy())
                return
            
            for i in range(start, len(candidates)):
                # Pruning 1: Skip duplicates to prevent duplicate combinations
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Pruning 2: If current sum + candidate > target, break early 
                # (Since array is sorted, all subsequent elements will also exceed the target)
                if current_sum + candidates[i] > target:
                    break

                current_comb.append(candidates[i])
                backtrack(i + 1, current_comb, current_sum + candidates[i])
                current_comb.pop()

        backtrack(0, [], 0)
        return res