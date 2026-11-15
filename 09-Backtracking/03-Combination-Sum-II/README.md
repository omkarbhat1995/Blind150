# Combination Sum II

**Difficulty:** Medium
**Category:** Backtracking

## Problem Description
You are given an array of integers `candidates`, which may contain duplicates, and a target integer `target`. Your task is to return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`.

Each element from `candidates` may be chosen **at most once** within a combination. The solution set must not contain duplicate combinations.

You may return the combinations in any order.

**Example 1:**
\`\`\`text
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
  [1,1,6],
  [1,2,5],
  [1,7],
  [2,6]
]
\`\`\`

**Example 2:**
\`\`\`text
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
  [1,2,2],
  [5]
]
\`\`\`

**Constraints:**
* `1 <= candidates.length <= 100`
* `1 <= candidates[i] <= 50`
* `1 <= target <= 30`

## Complexity Analysis
* **Time Complexity:** $\mathcal{O}(2^N)$ in the worst case, where $N$ is the number of elements in `candidates`. However, sorting the array and pruning paths that exceed the target or duplicate a previous branch heavily optimizes the actual runtime.
* **Space Complexity:** $\mathcal{O}(N)$ strictly for the recursion stack and the current combination list being maintained. The output list space is generally excluded from auxiliary space analysis.

## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```