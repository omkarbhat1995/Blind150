# Contains Duplicate

**Difficulty:** Easy  
**Category:** Arrays & Hashing  

## 📝 Problem Statement

Given an integer array `nums`, return `true` if any value appears more than once in the array, otherwise return `false`.

### Examples

**Example 1:**
> **Input:** `nums = [1, 2, 3, 3]`  
> **Output:** `true`

**Example 2:**
> **Input:** `nums = [1, 2, 3, 4]`  
> **Output:** `false`

### Constraints
* `0 <= nums.length <= 10^5`
* `-10^9 <= nums[i] <= 10^9`

---

## 💡 Approach

While a brute force solution of checking every element against every other element would work, it results in an highly inefficient `O(n^2)` time complexity. We can do much better by trading a little bit of space for a lot of speed.

By utilizing a **HashSet**, we can track the numbers we have seen so far as we iterate through the array. If we encounter a number that already exists in our set, we immediately know a duplicate exists and return `true`. If we finish the iteration without finding any duplicates, we return `false`.

### ⏱️ Complexity
* **Time Complexity:** `O(n)` — We iterate through the array at most once. Hash set insertions and lookups take `O(1)` time on average.
* **Space Complexity:** `O(n)` — In the worst-case scenario (an array with no duplicates), the hash set will need to store all `n` elements of the input array.

---

## 🧪 Running the Tests

This repository includes custom unit tests to verify the solution against both standard LeetCode examples and tricky edge cases. 

To run the tests for this specific problem, execute the following command in your terminal from the root directory:

```bash
pytest 01-Arrays-and-Hashing/01-Contains-Duplicate/test_solution.py -v