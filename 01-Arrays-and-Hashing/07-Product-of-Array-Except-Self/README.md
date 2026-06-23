# Product of Array Except Self

**Difficulty:** Medium  
**Category:** Arrays & Hashing  

## 📝 Problem Statement

Given an integer array `nums`, return an array `output` where `output[i]` is the product of all the elements of `nums` except `nums[i]`.

Each product is guaranteed to fit in a 32-bit integer.

**Follow-up:** Could you solve it in `O(n)` time without using the division operation?

### Examples

**Example 1:**
> **Input:** `nums = [1, 2, 4, 6]`  
> **Output:** `[48, 24, 12, 8]`

**Example 2:**
> **Input:** `nums = [-1, 0, 1, 2, 3]`  
> **Output:** `[0, -6, 0, 0, 0]`

### Constraints
* `2 <= nums.length <= 1000`
* `-20 <= nums[i] <= 20`

---

## 💡 Approach

The "no division" constraint forces us to think about how a product excluding the current element is formed. It is simply the product of all elements to the **left** of the current element (prefix) multiplied by the product of all elements to the **right** (postfix).

While we could create two separate arrays to store the prefix and postfix values, that would take `O(n)` extra space. We can optimize this to `O(1)` auxiliary space (excluding the output array):

1. Initialize our `output` array with `1`s.
2. **Left Pass (Prefix):** Iterate through the array from left to right. For each element, set `output[i]` to the current running prefix product, then multiply the prefix tracker by `nums[i]`.
3. **Right Pass (Postfix):** Iterate through the array from right to left. For each element, multiply `output[i]` by the current running postfix product, then multiply the postfix tracker by `nums[i]`.

### ⏱️ Complexity
* **Time Complexity:** `O(n)` — We make exactly two distinct passes through the array, scaling linearly with the size of `nums`.
* **Space Complexity:** `O(1)` — The problem explicitly states that the output array does not count toward space complexity. We only use two integer variables (`prefix` and `postfix`) for our logic.

---

## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:

`pytest 01-Arrays-and-Hashing/07-Product-of-Array-Except-Self/test_solution.py -v`