class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing brackets to their corresponding opening brackets
        closeToOpen = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c in closeToOpen:
                # If stack is not empty and top of stack matches the correct open bracket
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                # It's an opening bracket, push to stack
                stack.append(c)
                
        # Return True only if the stack is completely empty
        return True if not stack else False