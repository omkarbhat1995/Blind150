# Merge Two Sorted Linked Lists

## Problem Statement

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
The new list should be made up of nodes from `list1` and `list2`.

**Example 1:**
- **Input:** `list1 = [1,2,4]`, `list2 = [1,3,5]`
- **Output:** `[1,1,2,3,4,5]`

**Example 2:**
- **Input:** `list1 = []`, `list2 = [1,2]`
- **Output:** `[1,2]`

**Example 3:**
- **Input:** `list1 = []`, `list2 = []`
- **Output:** `[]`

**Constraints:**
- 0 <= The length of each list <= 100.
- -100 <= Node.val <= 100

## Approach

The most optimal way to solve this is by using a **Two-Pointer** approach alongside a **Dummy Node**. 

1. Create a `dummy` node to act as the starting point of our merged list and a `tail` pointer to track the end of our growing list.
2. Traverse both lists simultaneously using a `while` loop as long as both `list1` and `list2` are not null.
3. Compare the values of the current nodes in both lists. Append the smaller node to the `tail` and advance the corresponding list pointer.
4. Once one list is exhausted, append the remainder of the other list directly to the `tail`.
5. Return `dummy.next` as the true head of the merged list.

## Complexity
- **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the lengths of `list1` and `list2`. We traverse each node at most once.
- **Space Complexity:** $O(1)$. We are strictly manipulating existing pointers and not allocating any new scaling memory.

## Testing
To run the custom test suite:
```bash
pytest test_solution.py -v