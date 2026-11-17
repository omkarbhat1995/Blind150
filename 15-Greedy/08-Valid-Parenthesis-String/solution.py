class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        Validates the parenthesis string using a Greedy approach.
        We track the minimum and maximum possible number of open left parentheses.
        """
        min_open = 0  # The minimum possible open '(' we must match
        max_open = 0  # The maximum possible open '(' we could have
        
        for char in s:
            if char == "(":
                min_open += 1
                max_open += 1
            elif char == ")":
                min_open -= 1
                max_open -= 1
            else:
                # Wildcard '*' can be ')', '(', or empty
                min_open -= 1  # Treat as ')'
                max_open += 1  # Treat as '('
            
            # If the maximum possible open parentheses is negative, 
            # there are too many ')' to ever be valid.
            if max_open < 0:
                return False
            
            # The minimum open parentheses can never be negative 
            # (a ')' cannot match an empty string or a future '(').
            # We reset min_open to 0 if it drops below zero.
            min_open = max(min_open, 0)
            
        # The string is valid if it's mathematically possible to have exactly 0 open parentheses left
        return min_open == 0