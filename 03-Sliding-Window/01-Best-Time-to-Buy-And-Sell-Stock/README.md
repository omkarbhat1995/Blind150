# Best Time to Buy and Sell Stock

**Difficulty:** Easy
**Category:** Sliding Window / Arrays

## Problem Description

You are given an integer array `prices` where `prices[i]` is the price of NeetCoin on the `i`th day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be `0`.

### Examples

**Example 1:**
- **Input:** `prices = [10, 1, 5, 6, 7, 1]`
- **Output:** `6`
- **Explanation:** Buy `prices[1]` (price = 1) and sell `prices[4]` (price = 7), profit = 7 - 1 = 6.

**Example 2:**
- **Input:** `prices = [10, 8, 7, 5, 2]`
- **Output:** `0`
- **Explanation:** No profitable transactions can be made, thus the max profit is 0.

### Constraints
- `1 <= prices.length <= 100`
- `0 <= prices[i] <= 100`

## Optimal Approach

The optimal way to solve this is using a single-pass sliding window approach. We track the minimum price seen so far (our buying day) and the maximum profit we can achieve by selling on the current day. 

### Complexity
- **Time Complexity:** $O(n)$ where $n$ is the length of the `prices` array. We only iterate through the array once.
- **Space Complexity:** $O(1)$ since we only use a few variables to track the minimum price and maximum profit.

## How to Run the Tests
This directory contains a complete test suite using Python's built-in `unittest` framework.

1. Ensure you have Python installed on your system.
2. Open your terminal and navigate to the directory containing these files.
3. Run the test file:
`pytest .\test_solution.py -v`