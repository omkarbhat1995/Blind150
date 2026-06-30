# Reorder Linked List

## Problem Statement

You are given the head of a singly linked-list. The positions of a linked list of length = `n` can initially be represented as:
`[0, 1, 2, ..., n-2, n-1]`

Reorder the nodes of the linked list to be in the following order:
`[0, n-1, 1, n-2, 2, n-3, ...]`

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

**Example 1:**
- **Input:** `head = [2,4,6,8]`
- **Output:** `[2,8,4,6]`

**Example 2:**
- **Input:** `head = [2,4,6,8,10]`
- **Output:** `[2,10,4,8,6]`

**Constraints:**
- 1 <= Length of the list <= 1000.
- 1 <= Node.val <= 1000

## Approach

This problem is optimally solved by breaking it down into three distinct, classic linked list operations:
1. **Find the Middle:** Use the fast and slow pointer technique (Floyd's Tortoise and Hare) to locate the midpoint of the linked list.
2. **Reverse the Second Half:** Once the middle is found, reverse the entire second half of the linked list in-place.
3. **Merge the Halves:** Use two pointers (one at the beginning of the first half, one at the beginning of the reversed second half) to alternately merge the nodes together.

## Complexity
- **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the linked list. Finding the middle, reversing the half, and merging all take linear time.
- **Space Complexity:** $O(1)$. We are only manipulating existing pointers and do not allocate any scaling extra memory.

## Testing
To run the custom test suite:
```bash
pytest test_solution.py -v