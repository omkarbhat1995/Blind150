# Copy Linked List with Random Pointer

## Problem Statement

You are given the `head` of a linked list of length `n`. Unlike a singly linked list, each node contains an additional pointer `random`, which may point to any node in the list, or `null`.

Create a **deep copy** of the list.

The deep copy should consist of exactly `n` new nodes, each including:
- The original value `val` of the copied node
- A `next` pointer to the new node corresponding to the `next` pointer of the original node
- A `random` pointer to the new node corresponding to the `random` pointer of the original node

*Note: None of the pointers in the new list should point to nodes in the original list.*

Return the head of the copied linked list.

**Example 1:**
- **Input:** `head = [[3,null],[7,3],[4,0],[5,1]]`
- **Output:** `[[3,null],[7,3],[4,0],[5,1]]`

**Example 2:**
- **Input:** `head = [[1,null],[2,2],[3,2]]`
- **Output:** `[[1,null],[2,2],[3,2]]`

**Constraints:**
- 0 <= n <= 100
- -100 <= Node.val <= 100
- Node values are not guaranteed to be unique.
- `random` is null or is pointing to some node in the linked list.

## Approach

This problem is optimally solved using a **Two-Pass Hash Map** approach. 

1. **Pass 1 (Create Nodes):** Traverse the original linked list. For every node, create a brand new node with the same value. Store the mapping of the `original_node` to the `new_node` in a Hash Map.
2. **Pass 2 (Assign Pointers):** Traverse the original list a second time. Using our Hash Map, we can look up the newly created copy for the current node, and assign its `next` and `random` pointers to the newly created copies of the original `next` and `random` nodes.
3. Return the copied head from the Hash Map.

## Complexity
- **Time Complexity:** O(n), where n is the number of nodes in the linked list. We traverse the list exactly twice.
- **Space Complexity:** O(n). We use a Hash Map to store the mapping of all n original nodes to their copies.

## Testing
To run the custom test suite:
```bash
pytest test_solution.py -v