# Valid Palindrome

**Difficulty:** Easy
**Topics:** Two Pointers, String

## Problem Statement
Given a string `s`, return `true` if it is a palindrome, otherwise return `false`.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

**Note:** Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

## Examples

**Example 1:**
> **Input:** `s = "Was it a car or a cat I saw?"`
> **Output:** `true`
> **Explanation:** After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

**Example 2:**
> **Input:** `s = "tab a cat"`
> **Output:** `false`
> **Explanation:** "tabacat" is not a palindrome.

## Constraints
* `1 <= s.length <= 1000`
* `s` is made up of only printable ASCII characters.

## Optimal Approach & Complexity
* **Time Complexity:** O(n), where n is the length of the string `s`. We traverse the string with two pointers at most once.
* **Space Complexity:** O(1). We only use two pointers, requiring constant extra space, avoiding the need to build a new filtered string in memory.

## How to Run Tests
From the root directory, run the following command to execute the test suite for this problem:

