# Kth Largest Element in a Stream
Difficulty: Easy

Category: Heap / Priority Queue

## Problem Description
Design a class to find the kth largest integer in a stream of values, including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.Implement the following methods:constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.
---
Example 1:
Input: ["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]
Output:[null, 3, 3, 3, 5, 6]

Explanation:
KthLargest kthLargest = new KthLargest(3, [1, 2, 3, 3]);
kthLargest.add(3); // return 3
kthLargest.add(5); // return 3
kthLargest.add(6); // return 3
kthLargest.add(7); // return 5
kthLargest.add(8); // return 6
Constraints:1 <= k <= 10000 <= nums.length <= 1000-1000 <= nums[i] <= 1000-1000 <= val <= 1000.

There will always be at least k integers in the stream when you search for the kth integer.
---
## Complexity Analysis
* Time Complexity:__init__: $\mathcal{O}(N \log N)$ or $\mathcal{O}(N + (N-k) \log k)$ to build the initial heap of size $k$.add: $\mathcal{O}(\log k)$ because the heap size is strictly maintained at $k$.
* Space Complexity: $\mathcal{O}(k)$ to store the elements in the Min-Heap.

---

## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest 01-Arrays-and-Hashing/07-Product-of-Array-Except-Self/test_solution.py -v`
```