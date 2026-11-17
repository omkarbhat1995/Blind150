# Hand of Straights

**Difficulty:** Medium
**Category:** Greedy / Heap / Hash Map

## Problem Description
You are given an integer array `hand` where `hand[i]` is the value written on the `ith` card and an integer `groupSize`.

You want to rearrange the cards into groups so that each group is of size `groupSize`, and card values are consecutively increasing by 1.

Return `true` if it's possible to rearrange the cards in this way, otherwise, return `false`.
---
**Example 1:**
```text
Input: hand = [1,2,4,2,3,5,3,4], groupSize = 4
Output: true
Explanation: The cards can be rearranged as [1,2,3,4] and [2,3,4,5].
```
**Example 2:**
```text
Input: hand = [1,2,3,3,4,5,6,7], groupSize = 4
Output: false
Explanation: The closest we can get is [1,2,3,4] and [3,5,6,7], but the cards in the second group are not consecutive.
```
---
**Constraints:** 
* `1 <= hand.length <= 10000`
* `0 <= hand[i] <= 1000`
* `1 <= groupSize <= hand.length`
---
## Complexity Analysis
* **Time Complexity:** $\mathcal{O}(N \log N)$ where $N$ is the number of elements in hand. Constructing the frequency map takes $\mathcal{O}(N)$ time. Heapifying the unique keys takes $\mathcal{O}(U)$ where $U \le N$. Popping from the heap and processing elements takes $\mathcal{O}(N \log U)$ in the worst case.
* **Space Complexity:** $\mathcal{O}(N)$ to store the frequencies in the Hash Map and the unique keys in the Min-Heap.   


---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```