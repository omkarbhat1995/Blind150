# Reverse Nodes in k-Group

**Difficulty:** Hard
**Topics:** Linked List, Recursion, Two Pointers

## Problem Description

You are given the `head` of a singly linked list and a positive integer `k`.

You must reverse the first `k` nodes in the linked list, and then reverse the next `k` nodes, and so on. If there are fewer than `k` nodes left, leave the nodes as they are.

Return the modified list after reversing the nodes in each group of `k`.

You are only allowed to modify the nodes' `next` pointers, not the values of the nodes.

## Approach: Iterative Pointer Manipulation

To achieve $O(1)$ space complexity, we must reverse the groups in place. 

1. **Dummy Node:** We initialize a dummy node that points to the head of the list. This helps us manage the `prev` pointers easily, especially when reversing the very first group.
2. **Finding the $k$-th Node:** We use a helper function to jump `k` steps ahead. If we reach the end of the list before taking `k` steps, we leave the remaining nodes as they are and terminate.
3. **Reversing the Group:** Once we identify a valid group of `k` nodes, we isolate it and perform a standard linked list reversal.
4. **Stitching:** We carefully update the pointers of the node *before* the group (`groupPrev`) and the node *after* the group (`groupNext`) to reconnect our newly reversed section back into the main list.
5. **Advancing:** We update our `groupPrev` to point to the last node of our newly reversed group, and repeat the process.

## Complexity
- **Time Complexity:** $O(n)$ where $n$ is the total number of nodes in the linked list. Each node is visited twice at most (once when counting `k`, and once during reversal).
- **Space Complexity:** $O(1)$. We only use a few temporary pointers to manipulate the list in place.