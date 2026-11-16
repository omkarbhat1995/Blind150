from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generates all well-formed parentheses strings for n pairs.
        Uses a depth-first search (DFS) backtracking approach to maintain a 
        running balance of open and closed brackets.
        """
        res = []
        
        def backtrack(open_count: int, close_count: int, path: List[str]):
            # Base Case: When the sequence uses all open and closed brackets
            if open_count == n and close_count == n:
                res.append("".join(path))
                return
            
            # Decision 1: Add an open bracket if we haven't reached the limit 'n'
            if open_count < n:
                path.append("(")
                backtrack(open_count + 1, close_count, path)
                path.pop() # Backtrack
                
            # Decision 2: Add a closed bracket if it matches a previously opened bracket
            if close_count < open_count:
                path.append(")")
                backtrack(open_count, close_count + 1, path)
                path.pop() # Backtrack
                
        backtrack(0, 0, [])
        return res