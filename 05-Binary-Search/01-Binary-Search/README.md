# Binary Search

## Problem Description
You are given an array of distinct integers `nums`, sorted in ascending order, and an integer `target`.

Implement a function to search for `target` within `nums`. If it exists, then return its index, otherwise, return `-1`.

**Constraints:**
- `1 <= nums.length <= 10000`
- `-10000 < nums[i], target < 10000`
- All the integers in `nums` are unique.
- `nums` is sorted in ascending order.

## Approach: Two Pointers
Because the array is perfectly sorted, we don't need to check every single element. We can use a highly efficient **Binary Search** approach.

1. We initialize two pointers: `left` at the start of the array (index 0) and `right` at the end of the array (length - 1).
2. We loop as long as `left <= right`.
3. We calculate the `mid` index. *(Note: To prevent potential integer overflow in some languages, it is a best practice to calculate mid as `left + (right - left) // 2` rather than `(left + right) // 2`).*
4. We compare the element at `nums[mid]` with our `target`:
   - If they are equal, we found the target! Return `mid`.
   - If `nums[mid]` is less than the `target`, it means the target must be in the right half of our search space. We update `left = mid + 1`.
   - If `nums[mid]` is greater than the `target`, it means the target must be in the left half. We update `right = mid - 1`.
5. If the loop completes and we haven't returned anything, the target does not exist in the array. Return `-1`.

## Complexity
- **Time Complexity:** **O(log n)** - In every step, we are cutting the search space exactly in half.
- **Space Complexity:** **O(1)** - We only use a few integer variables (`left`, `right`, `mid`) regardless of the size of the array.