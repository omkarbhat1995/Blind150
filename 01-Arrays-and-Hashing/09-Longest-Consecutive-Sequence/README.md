# Longest Consecutive Sequence

**Difficulty:** Medium  
**Category:** Arrays & Hashing  

## 📝 Problem Statement

Given an array of integers `nums`, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly `1` greater than the previous element. The elements do not have to be consecutive in the original array.

**Requirement:** You must write an algorithm that runs in `O(n)` time.

### Examples

**Example 1:**
> **Input:** `nums = [2, 20, 4, 10, 3, 4, 5]`  
> **Output:** `4`  
> **Explanation:** The longest consecutive sequence is `[2, 3, 4, 5]`.

**Example 2:**
> **Input:** `nums = [0, 3, 2, 5, 4, 6, 1, 1]`  
> **Output:** `7`

### Constraints
* `0 <= nums.length <= 1000`
* `-10^9 <= nums[i] <= 10^9`

---

## 💡 Approach

The strict `O(n)` time constraint means we cannot sort the array (which would take `O(n log n)`). Instead, we can use a Hash Set to achieve `O(1)` lookups.

1. Convert the input array into a Hash Set. This automatically handles duplicates and allows instant lookups.
2. Iterate through the numbers in the set. For each number, check if it is the **start** of a sequence. A number is the start of a sequence if its left neighbor (`num - 1`) is *not* in the set.
3. If it is the start of a sequence, use a `while` loop to continuously check for the next consecutive numbers (`num + 1`, `num + 2`, etc.) in the set, keeping a running count.
4. Keep track of the maximum sequence length found.

By only initiating the inner `while` loop when we find the *start* of a sequence, we ensure that each number is processed at most twice (once in the outer loop, once in the inner loop). This guarantees our `O(n)` time complexity.

### ⏱️ Complexity
* **Time Complexity:** `O(n)` — Converting the array to a set takes `O(n)`. The `while` loop only runs for the lengths of the sequences, meaning each element is visited roughly `O(1)` times inside the loops.
* **Space Complexity:** `O(n)` — In the worst case, we store all `n` elements in the Hash Set.

---

## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:

```bash
pytest 01-Arrays-and-Hashing/09-Longest-Consecutive-Sequence/test_solution.py -v