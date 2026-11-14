# Two Sum

**Difficulty:** Easy  
**Category:** Arrays & Hashing  

## 📝 Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices `i` and `j` such that `nums[i] + nums[j] == target` and `i != j`.

You may assume that every input has exactly one pair of indices `i` and `j` that satisfy the condition. Return the answer with the smaller index first.

### Examples

**Example 1:**
> **Input:** `nums = [3, 4, 5, 6], target = 7`  
> **Output:** `[0, 1]`  
> **Explanation:** `nums[0] + nums[1] == 7`, so we return `[0, 1]`.

**Example 2:**
> **Input:** `nums = [4, 5, 6], target = 10`  
> **Output:** `[0, 2]`

**Example 3:**
> **Input:** `nums = [5, 5], target = 10`  
> **Output:** `[0, 1]`

### Constraints
* `2 <= nums.length <= 1000`
* `-10,000,000 <= nums[i] <= 10,000,000`
* `-10,000,000 <= target <= 10,000,000`
* Only one valid answer exists.

---

## 💡 Approach

A brute-force solution would involve checking every possible pair of numbers in the array to see if they add up to the target, which would take `O(n^2)` time. We can optimize this significantly by using extra space.

We can use a **Hash Map** to store the numbers we have seen so far and their corresponding indices. As we iterate through the array, for each number, we calculate its "complement" (the value needed to reach the target: `target - current_number`). 

We check if this complement already exists in our Hash Map:
1. If it does, we have found our pair! We return the index of the complement and our current index.
2. If it does not, we add the current number and its index to the Hash Map and continue.

### ⏱️ Complexity
* **Time Complexity:** `O(n)` — We traverse the list containing `n` elements exactly once. Each lookup and insertion in the Hash Map takes `O(1)` time on average.
* **Space Complexity:** `O(n)` — In the worst-case scenario, we might need to store `n - 1` elements in our Hash Map before finding the matching pair.

---

## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:

```bash
pytest 01-Arrays-and-Hashing/03-Two-Sum/test_solution.py -v
```