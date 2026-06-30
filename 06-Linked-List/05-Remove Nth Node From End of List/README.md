# Remove Nth Node From End of List

## Problem Statement

Given the `head` of a linked list and an integer `n`, remove the `nth` node from the end of the list and return its head.

**Example 1:**
- **Input:** `head = [1,2,3,4]`, `n = 2`
- **Output:** `[1,2,4]`

**Example 2:**
- **Input:** `head = [5]`, `n = 1`
- **Output:** `[]`

**Example 3:**
- **Input:** `head = [1,2]`, `n = 2`
- **Output:** `[2]`

**Constraints:**
- The number of nodes in the list is `sz`.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

## Approach

The most optimal way to solve this in a single pass is by using a **Two-Pointer** approach alongside a **Dummy Node**.

1. Create a `dummy` node that points to the `head` of the list. This handles the edge case where the node to be removed is the very first node in the list.
2. Initialize two pointers, `left` and `right`, both starting at the `dummy` node.
3. Move the `right` pointer forward exactly `n + 1` steps. This creates a gap of exactly `n` nodes between the `left` and `right` pointers.
4. Move both `left` and `right` pointers forward one step at a time until `right` reaches the end of the list (`null`). 
5. Because of the gap we created, the `left` pointer will now be sitting immediately *before* the node we want to remove.
6. Skip the target node by updating the pointer: `left.next = left.next.next`.
7. Return `dummy.next` as the true head of the modified list.

## Complexity
- **Time Complexity:** O(sz), where sz is the number of nodes in the linked list. We traverse the list exactly once.
- **Space Complexity:** O(1). We strictly manipulate existing pointers without allocating any scaling memory.

## Testing
To run the custom test suite:
```bash
pytest test_solution.py -v