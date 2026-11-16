from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all possible permutations of an array of unique integers.
        Utilizes a depth-first search (DFS) backtracking approach with a boolean state array 
        to track currently active elements in the recursion path.
        """
        res = []
        
        def backtrack(path: List[int], used: List[bool]):
            # Base Case: When the current permutation matches the length of the input array
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            # Decision Tree: Iterate through all numbers and branch if not currently in use
            for i in range(len(nums)):
                if not used[i]:
                    # Choose
                    used[i] = True
                    path.append(nums[i])
                    
                    # Explore
                    backtrack(path, used)
                    
                    # Un-choose (Backtrack)
                    path.pop()
                    used[i] = False
                    
        backtrack([], [False] * len(nums))
        return res