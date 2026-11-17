# Partition Labels

**Difficulty:** Medium
**Category:** Two Pointers / Greedy / Hash Table

## Problem Description
You are given a string `s` consisting of lowercase english letters.

We want to split the string into as many substrings as possible, while ensuring that each letter appears in at most one substring.

Return a list of integers representing the size of these substrings in the order they appear in the string.
---
**Example 1:**
```text
Input: s = "xyxxyzbzbbisl"
Output: [5, 5, 1, 1, 1]
Explanation: The string can be split into ["xyxxy", "zbzbb", "i", "s", "l"].
```
**Example 2:**
```text
Input: s = "abcabc"
Output: [6]
```
---
**Constraints:**
* `1 <= s.length <= 100`
---
## Complexity Analysis
* **Time Complexity:** $\mathcal{O}(n)$ where $n$ is the length of the string s. We iterate through the string twice: once to find the last occurrence of each character, and once to establish the partitions.
* **Space Complexity:** $\mathcal{O}(1)$ because the hash map used to store the last occurrences will contain at most 26 key-value pairs (one for each lowercase English letter), representing a constant space overhead regardless of the input string length.
---
---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```