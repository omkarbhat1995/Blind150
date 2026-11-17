# Valid Parenthesis String

**Difficulty:** Medium
**Category:** Greedy / String / Dynamic Programming

## Problem Description
You are given a string `s` which contains only three types of characters: `'('`, `')'` and `'*'`.

Return `true` if `s` is valid, otherwise return `false`.

A string is valid if it follows all of the following rules:
* Every left parenthesis `'('` must have a corresponding right parenthesis `')'`.
* Every right parenthesis `')'` must have a corresponding left parenthesis `'('`.
* Left parenthesis `'('` must go before the corresponding right parenthesis `')'`.
* A `'*'` could be treated as a right parenthesis `')'` character or a left parenthesis `'('` character, or as an empty string `""`.
---
**Example 1:**
```text
Input: s = "((**)"
Output: true
Explanation: One of the '*' could be a ')' and the other could be an empty string.
```
**Example 2:**
```text
Input: s = "(((*)"
Output: false
Explanation: The string is not valid because there is an extra '(' at the beginning, regardless of the extra '*'.
```

---

**Constraints:**
* `1 <= s.length <= 100`
* `s[i] is '(', ')', or '*'`

---
## Complexity Analysis
* **Time Complexity:**  $\mathcal{O}(n)$ where $n$ is the length of the string s. We iterate through the string exactly once.
* **Space Complexity:** $\mathcal{O}(1)$ as we only maintain two integer variables (min_open and max_open) to track the valid range of open parentheses dynamically.
---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```