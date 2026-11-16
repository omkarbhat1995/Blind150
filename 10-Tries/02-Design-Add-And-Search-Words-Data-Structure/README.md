# Design Add and Search Word Data Structure

**Difficulty:** Medium
**Category:** Trie / Design / String / Depth-First Search

## Problem Description
Design a data structure that supports adding new words and searching for existing words. 

Implement the `WordDictionary` class:
* `WordDictionary()` Initializes the object.
* `void addWord(word)` Adds `word` to the data structure, where it can be matched later.
* `bool search(word)` Returns `true` if there is any string in the data structure that matches `word` or `false` otherwise. `word` may contain dots `'.'` where dots can be matched with any letter.

**Example 1:**
```text
Input:
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["day"],["bay"],["may"],["say"],["day"],[".ay"],["b.."]]

Output:
[null, null, null, null, false, true, true, true]

Explanation:
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("day");
wordDictionary.addWord("bay");
wordDictionary.addWord("may");
wordDictionary.search("say"); // return false
wordDictionary.search("day"); // return true
wordDictionary.search(".ay"); // return true
wordDictionary.search("b.."); // return true
```
---
## Complexity Analysis
* **Time Complexity:**addWord: $\mathcal{O}(M)$ where $M$ is the length of the word.search: $\mathcal{O}(M)$ for well-defined words without dots. In the worst-case scenario with dots, the time complexity is $\mathcal{O}(26^D \cdot M)$ where $D$ is the number of dots, since we must use backtracking to explore all possible character paths.
* **Space Complexity:** $\mathcal{O}(N \cdot M)$ for storing $N$ words of length $M$ in the Trie structure, plus $\mathcal{O}(M)$ auxiliary stack space during the DFS search recursion.