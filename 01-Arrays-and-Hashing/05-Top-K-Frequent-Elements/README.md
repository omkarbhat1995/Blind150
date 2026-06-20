# Top K Frequent Elements

**Difficulty:** Medium  
**Category:** Arrays & Hashing  

## 📝 Problem Statement

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements within the array.

The test cases are generated such that the answer is always unique. You may return the output in any order.

### Examples

**Example 1:**
> **Input:** `nums = [1, 2, 2, 3, 3, 3], k = 2`  
> **Output:** `[2, 3]`

**Example 2:**
> **Input:** `nums = [7, 7], k = 1`  
> **Output:** `[7]`

### Constraints
* `1 <= nums.length <= 10^4`
* `-1000 <= nums[i] <= 1000`
* `1 <= k <= number of distinct elements in nums`

---

## 💡 Approach

A standard approach would be to count the frequencies using a Hash Map and then sort the map by its values, taking `O(N log N)` time. We could optimize this slightly using a Max Heap to get `O(N log k)` time. 

However, we can achieve a strict linear **`O(N)`** time complexity by using a modified **Bucket Sort**.

1. First, we count the frequencies of each number using a Hash Map.
2. Next, we create a "bucket" array where the *index* represents the frequency of a number, and the *value* at that index is a list of numbers that appear with that exact frequency. The maximum possible frequency is the length of the array itself.
3. Finally, we iterate backward through our bucket array (from highest frequency to lowest), appending elements to our result list until we have gathered `k` elements.

### ⏱️ Complexity
* **Time Complexity:** `O(n)` — We iterate through the array to count frequencies, iterate through the hash map to populate buckets, and iterate through the buckets to get the result. All loops are unnested and scale linearly with `n`.
* **Space Complexity:** `O(n)` — The Hash Map and the Bucket array both require memory proportional to the size of the input array.

---

## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:

```bash
pytest 01-Arrays-and-Hashing/05-Top-K-Frequent-Elements/test_solution.py -v