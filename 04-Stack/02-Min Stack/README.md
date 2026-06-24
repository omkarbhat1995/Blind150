# Min Stack

## Problem Description
Design a stack class that supports the `push`, `pop`, `top`, and `getMin` operations.

- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

**Constraint:** Each function must run in $O(1)$ time.

**Constraints:**
- $-2^{31} \le val \le 2^{31} - 1$
- `pop`, `top` and `getMin` will always be called on non-empty stacks.

## Approach: Two Stacks
To achieve $O(1)$ retrieval of the minimum value, a single standard stack is not enough because popping the minimum value would require us to search the entire stack for the new minimum. 

Instead, we can use **two stacks**:
1. `stack`: To keep track of the actual elements.
2. `min_stack`: To keep track of the minimum value at each level of the main stack.

When we push a value, we push it onto `stack`. We also push the minimum of the new value and the current minimum onto `min_stack`. When we pop, we pop from both stacks. This guarantees that `min_stack` always has the correct minimum value for the current state of `stack` right at its top.

## Complexity
- **Time Complexity:** $O(1)$ for `push`, `pop`, `top`, and `getMin`.
- **Space Complexity:** $O(n)$ where $n$ is the number of elements in the stack, as we are maintaining a secondary stack.