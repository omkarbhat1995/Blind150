# Evaluate Reverse Polish Notation

## Problem Description
You are given an array of strings `tokens` that represents a valid arithmetic expression in Reverse Polish Notation (RPN).

Return the integer that represents the evaluation of the expression.

**Rules:**
- The operands may be integers or the results of other operations.
- The operators include `'+'`, `'-'`, `'*'`, and `'/'`.
- Assume that division between integers always **truncates toward zero**.

**Constraints:**
- 1 <= tokens.length <= 1000.
- `tokens[i]` is "+", "-", "*", or "/", or a string representing an integer in the range [-200, 200].

## Approach: Stack
Reverse Polish Notation is naturally solved using a **Stack**. 
1. We iterate through the array of tokens one by one.
2. If the token is a number, we push it onto the stack.
3. If the token is an operator (`+`, `-`, `*`, `/`), we pop the top two numbers from the stack.
   - *Note:* The first number popped is the right operand, and the second number popped is the left operand.
4. We apply the operator to these two numbers and push the result back onto the stack.
5. Once all tokens have been processed, the final result will be the only element remaining in the stack.

*Language Edge Case:* In Python, standard integer division (`//`) floors towards negative infinity. To properly truncate towards zero for negative numbers, we use float division cast to an integer: `int(left / right)`.

## Complexity
- **Time Complexity:** O(n) - We traverse the list of tokens exactly once. Stack push and pop operations take O(1) time.
- **Space Complexity:** O(n) - In the worst-case scenario (an expression with many numbers before operations), the stack will grow proportionally to the number of tokens.