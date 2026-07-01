# Merge K Sorted Linked Lists

**Difficulty:** Hard
**Topics:** Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort

## Problem Description

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

## Approach: Priority Queue (Min-Heap)

Comparing the heads of `k` lists simultaneously would normally take $O(k)$ time per node. We can optimize this by utilizing a Min-Heap (Priority Queue). 

1. **Initialization:** We push the head node of each of the `k` linked lists into a Min-Heap. To avoid pointer comparison issues in Python, we push a tuple containing `(node_value, list_index, node)`.
2. **Merging:** We pop the smallest element from the heap and append it to our new merged list.
3. **Refilling:** If the popped node has a `.next` node, we push that next node into the heap.
4. **Completion:** We repeat this process until the heap is empty, returning the head of the newly merged list.

## Complexity
- **Time Complexity:** $O(N \log k)$ where `N` is the total number of nodes across all lists, and `k` is the number of linked lists. Each pop and push operation on the heap takes $O(\log k)$ time.
- **Space Complexity:** $O(k)$. The heap will store at most `k` elements at any given time (one node from each list).