# Longest Substring Without Repeating Characters

**Difficulty:** Medium
**Category:** Sliding Window / Strings

## Problem Description

Given a string `s`, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

### Examples

**Example 1:**
- **Input:** `s = "zxyzxyz"`
- **Output:** `3`
- **Explanation:** The string "xyz" is the longest without duplicate characters.

**Example 2:**
- **Input:** `s = "xxxx"`
- **Output:** `1`
- **Explanation:** The longest substring without duplicate characters is "x", with a length of 1.

### Constraints
- `0 <= s.length <= 1000`
- `s` may consist of printable ASCII characters.

## Optimal Approach

The most efficient way to solve this is using a **Sliding Window** approach combined with a Hash Map (or Dictionary). We use two pointers (`left` and `right`) to represent our window. As we iterate through the string with the `right` pointer, we store the most recent index of each character in the hash map. If we encounter a character that is already in our window, we instantly jump our `left` pointer to the index right after the previous occurrence of that character.

### Complexity
- **Time Complexity:** `O(n)` where `n` is the length of the string. We iterate through the string exactly once.
- **Space Complexity:** `O(m)` where `m` is the size of the character set (e.g., 128 for printable ASCII characters). Since this is bounded by a constant, it can also be considered `O(1)`.