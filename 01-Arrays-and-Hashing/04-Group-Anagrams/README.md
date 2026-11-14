# Group Anagrams

**Difficulty:** Medium  
**Category:** Arrays & Hashing  

## 📝 Problem Statement

Given an array of strings `strs`, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

### Examples

**Example 1:**
> **Input:** `strs = ["act", "pots", "tops", "cat", "stop", "hat"]`  
> **Output:** `[["hat"], ["act", "cat"], ["stop", "pots", "tops"]]`

**Example 2:**
> **Input:** `strs = ["x"]`  
> **Output:** `[["x"]]`

**Example 3:**
> **Input:** `strs = [""]`  
> **Output:** `[[""]]`

### Constraints
* `1 <= strs.length <= 1000`
* `0 <= strs[i].length <= 100`
* `strs[i]` is made up of lowercase English letters.

---

## 💡 Approach

A naive approach would be to sort every single string and group them by their sorted version. However, sorting takes `O(k log k)` time per string, which slows down as the strings get longer.

We can optimize this by building upon the logic from the "Valid Anagram" problem. Instead of sorting, we can count the frequency of each character (from 'a' to 'z') and use that count as our grouping key. 

Since Python lists are mutable and cannot be used as dictionary keys, we convert the frequency array of size 26 into a `tuple`. We map each tuple to a list of strings that share that exact character frequency.

### ⏱️ Complexity
* **Time Complexity:** `O(m * n)` — Where `m` is the total number of strings and `n` is the average length of a string. We iterate through every string, and for each string, we iterate through its characters to count them.
* **Space Complexity:** `O(m * n)` — In the worst-case scenario (no anagrams exist), our Hash Map will store every single string and its corresponding tuple key.

---

## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:

```bash
pytest 01-Arrays-and-Hashing/04-Group-Anagrams/test_solution.py -v
```