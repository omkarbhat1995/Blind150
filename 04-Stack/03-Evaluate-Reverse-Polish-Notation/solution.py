from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                # The first pop is the right operand, the second is the left operand
                right = stack.pop()
                left = stack.pop()
                
                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
                elif token == "*":
                    stack.append(left * right)
                elif token == "/":
                    # Use float division and cast to int to truncate towards zero
                    stack.append(int(left / right))
            else:
                # It's a number, push it to the stack
                stack.append(int(token))
                
        return stack[0]