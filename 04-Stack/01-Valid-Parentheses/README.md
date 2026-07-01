# Valid Parentheses

## Problem Description
Given a string `s` consisting of the following characters: `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`. 

The input string `s` is valid if and only if:
1. Every open bracket is closed by the same type of close bracket.
2. Open brackets are closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Constraints:**
- `1 <= s.length <= 1000`
- `s` consists of parentheses only `'()[]{}'`.

## Approach: Stack
The optimal way to validate matching pairs in a specific order is by using a **Stack**. 
1. We can use a Hash Map to map closing brackets to their corresponding opening brackets.
2. We iterate through the string character by character.
3. If we encounter an opening bracket, we push it onto the stack.
4. If we encounter a closing bracket, we check if the stack is non-empty and if the top of the stack is the matching opening bracket. If it is, we pop the opening bracket off the stack. If it isn't, the string is invalid.
5. In the end, if the stack is empty, it means every opening bracket was properly closed.

## Complexity
- **Time Complexity:** O(n) - We traverse the string exactly once, and stack push/pop operations take O(1) time.
- **Space Complexity:** O(n) - In the worst case (e.g., all opening brackets), the stack will grow to the size of the string.