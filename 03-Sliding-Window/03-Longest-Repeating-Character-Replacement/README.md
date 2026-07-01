# Longest Repeating Character Replacement

**Difficulty:** Medium
**Category:** Sliding Window / Strings

## Problem Description

You are given a string `s` consisting of only uppercase english characters and an integer `k`. You can choose up to `k` characters of the string and replace them with any other uppercase English character.

After performing at most `k` replacements, return the length of the longest substring which contains only one distinct character.

### Examples

**Example 1:**
- **Input:** `s = "XYYX", k = 2`
- **Output:** `4`
- **Explanation:** Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

**Example 2:**
- **Input:** `s = "AAABABB", k = 1`
- **Output:** `5`
- **Explanation:** Replace the one 'B' in the middle to get "AAAAABB", which gives a repeating 'A' string of length 5.

### Constraints
- `1 <= s.length <= 1000`
- `0 <= k <= s.length`
- `s` consists of only uppercase English letters.

## Optimal Approach

We use a **Sliding Window** combined with a frequency map. The core logic relies on this equation: 
`(Length of Current Window) - (Count of Most Frequent Character in Window) <= k`

If this condition is true, our window is valid because the number of characters we need to replace is within our allowed limit `k`. If the condition becomes false, the window is invalid, and we must shrink it by moving the `left` pointer forward.

To optimize further, we don't even need to strictly decrement our historical `max_frequency` when shrinking the window. The overall maximum window size is only ever bounded by the highest frequency we've seen so far.

### Complexity
- **Time Complexity:** $O(n)$ where $n$ is the length of the string. Both the left and right pointers only move forward.
- **Space Complexity:** $O(1)$ (or $O(26)$) since the frequency hash map will store at most 26 uppercase English characters.