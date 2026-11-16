# Implement Trie (Prefix Tree)

**Difficulty:** Medium
**Category:** Trees / Trie

## Problem Description
A prefix tree (also known as a trie) is a tree data structure used to efficiently store and retrieve keys in a set of strings. Some applications of this data structure include auto-complete and spell checker systems.

Implement the `PrefixTree` class:
* `PrefixTree()` Initializes the prefix tree object.
* `void insert(String word)` Inserts the string `word` into the prefix tree.
* `boolean search(String word)` Returns `true` if the string `word` is in the prefix tree (i.e., was inserted before), and `false` otherwise.
* `boolean startsWith(String prefix)` Returns `true` if there is a previously inserted string `word` that has the prefix `prefix`, and `false` otherwise.
---
**Example 1:**
```text
Input:
["PrefixTree", "insert", "dog", "search", "dog", "search", "do", "startsWith", "do", "insert", "do", "search", "do"]
Output:
[null, null, true, false, true, null, true]

Explanation:
PrefixTree prefixTree = new PrefixTree();
prefixTree.insert("dog");
prefixTree.search("dog");   // return true
prefixTree.search("do");    // return false
prefixTree.startsWith("do"); // return true
prefixTree.insert("do");
prefixTree.search("do");    // return true

```
---
## Complexity Analysis
* **Time Complexity:**   insert: $\mathcal{O}(m)$ where $m$ is the length of the word.   search: $\mathcal{O}(m)$ where $m$ is the length of the word.   startsWith: $\mathcal{O}(m)$ where $m$ is the length of the prefix.   
* **Space Complexity:** $\mathcal{O}(N \cdot m)$ in the worst case, where $N$ is the number of inserted words and $m$ is the maximum length of a word, representing the storage of the character nodes. 
---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```