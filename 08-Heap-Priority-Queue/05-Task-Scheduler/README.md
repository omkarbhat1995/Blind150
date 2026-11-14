# Task Scheduler

**Difficulty:** Medium
**Category:** Array / Greedy / Math

## Problem Description
You are given an array of CPU tasks `tasks`, where `tasks[i]` is an uppercase English character from A to Z. You are also given an integer `n`.

Each CPU cycle allows the completion of a single task, and tasks may be completed in any order. The only constraint is that identical tasks must be separated by at least `n` CPU cycles to cool down the CPU.

Return the minimum number of CPU cycles required to complete all tasks.

**Example 1:**
```text
Input: tasks = ["X","X","Y","Y"], n = 2
Output: 5
Explanation: A possible sequence is: X -> Y -> idle -> X -> Y.
```
**Example 2:**
```text
Input: tasks = ["A","A","A","B","C"], n = 3
Output: 9
Explanation: A possible sequence is: A -> B -> C -> Idle -> A -> Idle -> Idle -> Idle -> A.
```

Complexity Analysis
* Time Complexity: $\mathcal{O}(N)$ where $N$ is the total number of tasks. Counting the frequencies takes linear time, and finding the max frequency takes $\mathcal{O}(1)$ since the dictionary contains at most 26 elements.
* Space Complexity: $\mathcal{O}(1)$ because the Counter dictionary will only ever store up to 26 key-value pairs (for uppercase English letters), regardless of the size of the input array.