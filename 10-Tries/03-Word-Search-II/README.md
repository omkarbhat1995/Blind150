# Word Search II

**Difficulty:** Hard
**Category:** Trie / Backtracking / Depth-First Search

## Problem Description
Given an `m x n` `board` of characters and a list of strings `words`, return all words that are present in the grid.

For a word to be present it must be possible to form the word with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.
---
**Example 1:**
```text
Input: 
board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
], 
words = ["bat","cat","back","backend","stack"]

Output: ["cat","back","backend"]
```
**Example 2:**
```text
Input: 
board = [
  ["x","o"],
  ["x","o"]
], 
words = ["xoxo"]

Output: []
```
---
Constraints:

* `1 <= board.length, board[i].length <= 12`
* `board[i] consists only of lowercase English letters.`
* `1 <= words.length <= 30,000`
* `1 <= words[i].length <= 10`
* `words[i] consists only of lowercase English letters.`
All strings within words are distinct.
---
## Complexity Analysis
* **Time Complexity:** $\mathcal{O}(W \cdot L + M \cdot N \cdot 3^{L-1})$ where $W$ is the number of words, $L$ is the maximum length of a word, $M$ is the number of rows, and $N$ is the number of columns. Building the Trie takes $\mathcal{O}(W \cdot L)$. The DFS traversal from each cell takes $\mathcal{O}(3^{L-1})$ since we have 3 choices at each step after the first character, up to a maximum depth of $L=10$.
* **Space Complexity:**  $\mathcal{O}(W \cdot L)$ to store all words in the Trie data structure, plus $\mathcal{O}(L)$ for the recursion stack during the depth-first search.   
---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```