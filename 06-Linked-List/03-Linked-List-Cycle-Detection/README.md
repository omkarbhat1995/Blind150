# Linked List Cycle Detection

## Problem Statement

Given the beginning of a linked list `head`, return `true` if there is a cycle in the linked list. Otherwise, return `false`.

There is a cycle in a linked list if at least one node in the list can be visited again by following the `next` pointer. Internally, `index` determines the index of the beginning of the cycle, if it exists. The tail node of the list will set its `next` pointer to the `index`-th node. If `index = -1`, then the tail node points to null and no cycle exists.

*Note: `index` is not given to you as a parameter.*

**Example 1:**
- **Input:** `head = [1,2,3,4]`, `index = 1`
- **Output:** `true`
- **Explanation:** There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

**Example 2:**
- **Input:** `head = [1,2]`, `index = -1`
- **Output:** `false`

**Constraints:**
- 0 <= Length of the list <= 1000
- -1000 <= Node.val <= 1000
- `index` is -1 or a valid index in the linked list.

## Approach

This problem is optimally solved using **Floyd's Tortoise and Hare Algorithm** (a fast and slow pointer approach).

1. Initialize two pointers, `slow` and `fast`, both starting at the `head` of the linked list.
2. Traverse the list moving the `slow` pointer forward by one node and the `fast` pointer forward by two nodes at a time.
3. If there is no cycle, the `fast` pointer will eventually reach the end of the list (`null`). We can safely return `false`.
4. If a cycle exists, the `fast` pointer will loop around and eventually land on the exact same node as the `slow` pointer. When they meet, we return `true`.

## Complexity
- **Time Complexity:** O(n) where n is the number of nodes in the linked list. In the worst-case scenario (no cycle), we traverse the list once. If there is a cycle, the fast pointer will catch the slow pointer in at most O(n) steps.
- **Space Complexity:** O(1). We only use two pointers, requiring constant extra memory regardless of the list size.

## Testing
To run the custom test suite:
```bash
pytest test_solution.py -v