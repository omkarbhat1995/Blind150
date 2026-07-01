# Minimum Window Substring

**Difficulty:** Hard
**Category:** Sliding Window / Hash Maps

## Problem Description

Given two strings `s` and `t`, return the shortest substring of `s` such that every character in `t`, including duplicates, is present in the substring. If such a substring does not exist, return an empty string `""`.

You may assume that the correct output is always unique.

### Examples

**Example 1:**
- **Input:** `s = "OUZODYXAZV", t = "XYZ"`
- **Output:** `"YXAZ"`
- **Explanation:** `"YXAZ"` is the shortest substring that includes "X", "Y", and "Z" from string `t`.

**Example 2:**
- **Input:** `s = "xyz", t = "xyz"`
- **Output:** `"xyz"`
- **Explanation:** The entire string `s` is the minimum window.

**Example 3:**
- **Input:** `s = "x", t = "xy"`
- **Output:** `""`
- **Explanation:** `t` includes characters not present in `s`, making it impossible.

### Constraints
- `1 <= s.length <= 1000`
- `1 <= t.length <= 1000`
- `s` and `t` consist of uppercase and lowercase English letters.

## Optimal Approach

This is solved efficiently using a **Sliding Window** and two hash maps (or arrays). 
1. We first count the frequencies of the characters we need from `t`.
2. We use two pointers (`left` and `right`) to expand a window across `s`. We track the characters currently in our window.
3. We maintain two integer variables: `have` (how many character requirements we currently meet) and `need` (the total number of unique characters in `t`).
4. Whenever `have == need`, our window is valid. We then increment the `left` pointer to shrink the window as much as possible until `have < need`, keeping track of the minimum window size observed.

### Complexity
- **Time Complexity:** $O(|s| + |t|)$ where $|s|$ and $|t|$ are the lengths of the strings. Each character in `s` is visited at most twice (once by the right pointer, once by the left).
- **Space Complexity:** $O(1)$. While we use a Hash Map, the maximum number of unique characters is 52 (uppercase and lowercase English letters), which operates in $O(1)$ constant space.