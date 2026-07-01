# Search in Rotated Sorted Array

## Problem Description
You are given an array of length `n` which was originally sorted in ascending order. It has now been rotated between `1` and `n` times. 

Given the rotated sorted array `nums` and an integer `target`, return the index of `target` within `nums`, or `-1` if it is not present.

You may assume all elements in the sorted rotated array `nums` are unique.

**Constraint:** A solution that runs in O(n) time is trivial, you must write an algorithm that runs in O(log n) time.

**Constraints:**
- `1 <= nums.length <= 1000`
- `-1000 <= nums[i] <= 1000`
- `-1000 <= target <= 1000`
- All values of `nums` are unique.
- `nums` is an ascending array that is possibly rotated.

## Approach: Modified Binary Search
To achieve O(log n) time complexity, we must use Binary Search. The tricky part is that the array is rotated, meaning a standard binary search will fail. However, if we split the array at any `mid` point, **at least one half of the array will always be strictly sorted**. 

1. We initialize our `left` and `right` pointers to the start and end of the array.
2. While `left <= right`, we calculate the `mid` index and check if `nums[mid] == target`. If so, we return `mid`.
3. If we haven't found the target, we determine which half of our current window is perfectly sorted:
   - **Left Half is Sorted (`nums[left] <= nums[mid]`):** We check if our `target` falls within this sorted range (`nums[left] <= target < nums[mid]`). If it does, we narrow our search to the left half (`right = mid - 1`). If it doesn't, the target must be in the right half (`left = mid + 1`).
   - **Right Half is Sorted (`nums[mid] <= nums[right]`):** We check if our `target` falls within this sorted range (`nums[mid] < target <= nums[right]`). If it does, we narrow our search to the right half (`left = mid + 1`). If it doesn't, the target must be in the left half (`right = mid - 1`).
4. If the loop finishes and we haven't returned an index, the `target` is not in the array, so we return `-1`.

## Complexity
- **Time Complexity:** O(log n) - We eliminate half of the remaining array elements at every step.
- **Space Complexity:** O(1) - We are only using a few pointers, requiring no extra memory.