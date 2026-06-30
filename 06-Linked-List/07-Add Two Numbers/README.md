# Add Two Numbers

## Problem Statement

You are given two **non-empty** linked lists, `l1` and `l2`, where each represents a non-negative integer.
The digits are stored in **reverse order**, e.g. the number 321 is represented as `1 -> 2 -> 3 ->` in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.

**Example 1:**
- **Input:** `l1 = [1,2,3]`, `l2 = [4,5,6]`
- **Output:** `[5,7,9]`
- **Explanation:** 321 + 654 = 975.

**Example 2:**
- **Input:** `l1 = [9]`, `l2 = [9]`
- **Output:** `[8,1]`

**Constraints:**
- 1 <= l1.length, l2.length <= 100.
- 0 <= Node.val <= 9

## Approach

This problem is optimally solved using a **Single Pass** approach with a **Dummy Node** and a **Carry** tracker.

1. Create a `dummy` node to act as the head of our newly created linked list, and a `curr` pointer to track our current position.
2. Initialize a `carry` integer to `0`.
3. Traverse both `l1` and `l2` simultaneously using a `while` loop. The loop should continue as long as `l1` is not null, `l2` is not null, OR `carry` is greater than `0`. (The carry condition ensures we don't forget an extra digit at the very end).
4. In each iteration, extract the values from `l1` and `l2` (defaulting to `0` if one list has been fully traversed).
5. Calculate the sum of the two values plus the `carry`. 
6. Update the `carry` for the next iteration (sum integer division by 10) and append the new digit (sum modulo 10) to our `curr` node.
7. Step our `curr`, `l1`, and `l2` pointers forward.
8. Return `dummy.next` as the true head of the new list.

## Complexity
- **Time Complexity:** O(max(m, n)), where m and n are the lengths of `l1` and `l2`. We iterate at most the length of the longer list (plus one potential iteration for a final carry).
- **Space Complexity:** O(max(m, n)). The length of the new list is at most max(m, n) + 1.

## Testing
To run the custom test suite:
```bash
pytest test_solution.py -v