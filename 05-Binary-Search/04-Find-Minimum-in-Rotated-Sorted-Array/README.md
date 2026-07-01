# Find Minimum in Rotated Sorted Array

## Problem Description
You are given an array of length `n` which was originally sorted in ascending order. It has now been rotated between `1` and `n` times. 
The array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array `nums` are unique, return the minimum element of this array.

**Constraint:** A solution that runs in $O(n)$ time is trivial. You must write an algorithm that runs in $O(\log n)$ time.

**Constraints:**
- `1 <= nums.length <= 1000`
- `-1000 <= nums[i] <= 1000`
- All elements in `nums` are unique.

## Approach: Modified Binary Search
To achieve $O(\log n)$ time complexity, we must use Binary Search. The tricky part is that the array is rotated, meaning it is split into two separate sorted portions. 

1. We initialize our `left` and `right` pointers to the start and end of the array.
2. We keep a `res` variable to track the current minimum found.
3. While `left <= right`, we first check if the subarray from `left` to `right` is already perfectly sorted (i.e., `nums[left] < nums[right]`). If it is, the minimum in this window is just `nums[left]`, we update `res` and break out of the loop.
4. If it's not perfectly sorted, we calculate the `mid` index and update our `res` with `nums[mid]`.
5. Now we must decide which half to search:
   - If `nums[mid] >= nums[left]`, it means the `mid` element belongs to the left sorted portion. The true minimum must be strictly in the right sorted portion, so we move our pointer: `left = mid + 1`.
   - If `nums[mid] < nums[left]`, it means the `mid` element belongs to the right sorted portion. The true minimum could either be the `mid` element itself (which we've already recorded) or somewhere to its left, so we move our pointer: `right = mid - 1`.

## Complexity
- **Time Complexity:** $O(\log n)$ - We eliminate half of the remaining array elements at every step of our binary search.
- **Space Complexity:** $O(1)$ - We are only using a few pointers to perform the search, requiring no extra memory.