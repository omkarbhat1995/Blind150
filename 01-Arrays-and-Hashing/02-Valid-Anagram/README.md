# Valid Anagram

**Difficulty:** Easy  
**Category:** Arrays & Hashing  

## 📝 Problem Statement

Given two strings `s` and `t`, return `true` if the two strings are anagrams of each other, otherwise return `false`.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

### Examples

**Example 1:**
> **Input:** `s = "racecar", t = "carrace"`  
> **Output:** `true`

**Example 2:**
> **Input:** `s = "jar", t = "jam"`  
> **Output:** `false`

### Constraints
* `1 <= s.length, t.length <= 5 * 10^4`
* `s` and `t` consist of lowercase English letters.

---

## 💡 Approach

A naive approach might involve sorting both strings and comparing them, but that would take `O(n log n)` time. We can achieve a linear time solution by counting the frequencies of each character.

Since the problem constraints guarantee that our strings only contain lowercase English letters, we don't need a dynamic Hash Map. We can use a fixed-size array of 26 integers. We iterate through the strings, incrementing the count for a character found in `s` and decrementing the count for a character found in `t`. If the strings are anagrams, all values in our frequency array will perfectly cancel out to `0` at the end.

### ⏱️ Complexity
* **Time Complexity:** `O(n + m)` — We iterate through both strings completely (where `n` and `m` are the lengths of `s` and `t`).
* **Space Complexity:** `O(1)` — We use an array of size 26 regardless of how large the input strings grow. Because the auxiliary space does not scale with the input size, it is strictly constant.

---

## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:

```bash
pytest 01-Arrays-and-Hashing/02-Valid-Anagram/test_solution.py -v