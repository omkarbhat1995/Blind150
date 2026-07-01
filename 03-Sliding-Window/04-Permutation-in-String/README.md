# Permutation in String

**Difficulty:** Medium
**Category:** Sliding Window / Two Pointers

## Problem Description

You are given two strings `s1` and `s2`.

Return `true` if `s2` contains a permutation of `s1`, or `false` otherwise. That means if a permutation of `s1` exists as a substring of `s2`, then return `true`.

Both strings only contain lowercase letters.

### Examples

**Example 1:**
- **Input:** `s1 = "abc", s2 = "lecabee"`
- **Output:** `true`
- **Explanation:** The substring "cab" is a permutation of "abc" and is present in "lecabee".

**Example 2:**
- **Input:** `s1 = "abc", s2 = "lecaabee"`
- **Output:** `false`
- **Explanation:** No contiguous substring in "lecaabee" is a permutation of "abc".

### Constraints
- `1 <= s1.length, s2.length <= 1000`
- `s1` and `s2` consist of lowercase English letters.

## Optimal Approach

Since a permutation merely means having the exact same characters with the exact same frequencies, we can use a **Sliding Window** coupled with frequency arrays. Because the strings only contain lowercase English letters, we can use two arrays of size 26 to tally the character counts.

We create a window of length `s1.length` and slide it across `s2`. At each step, we add the new character entering the window on the right to our frequency array and remove the old character leaving the window from the left. If the frequency array of our window ever perfectly matches the frequency array of `s1`, we have found a valid permutation.

### Complexity
- **Time Complexity:** $O(l_1 + l_2)$ where $l_1$ and $l_2$ are the lengths of `s1` and `s2`. Comparing two arrays of fixed size 26 takes $O(1)$ time, so the window slides in linear time.
- **Space Complexity:** $O(1)$ since we are strictly using frequency arrays of size 26, which do not scale with the size of the input strings.