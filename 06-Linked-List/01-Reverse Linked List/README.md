# Reverse Linked List

## Problem Statement

Given the beginning of a singly linked list `head`, reverse the list, and return the new beginning of the list.

**Example 1:**
- **Input:** `head = [0,1,2,3]`
- **Output:** `[3,2,1,0]`

**Example 2:**
- **Input:** `head = []`
- **Output:** `[]`

**Constraints:**
- `0 <= The length of the list <= 1000`
- `-1000 <= Node.val <= 1000`

## Approach

This solution utilizes an iterative approach with three pointers (`prev`, `curr`, and `nxt`) to reverse the links in place. 

1. Initialize `prev` as `None` and `curr` as the `head` of the list.
2. Traverse the list. In each step:
   - Save the next node (`nxt = curr.next`).
   - Reverse the current node's pointer (`curr.next = prev`).
   - Move the `prev` and `curr` pointers one step forward (`prev = curr`, `curr = nxt`).
3. Return `prev`, which will be pointing to the new head of the reversed list.

## Complexity
- **Time Complexity:** `O(n)` where `n` is the number of nodes in the linked list. We traverse the list exactly once.
- **Space Complexity:** `O(1)` as we only use a few pointers regardless of the size of the linked list.

## Testing
To run the custom test suite:
```bash
pytest test_solution.py -v