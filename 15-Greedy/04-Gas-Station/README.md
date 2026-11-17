# Gas Station

**Difficulty:** Medium
**Category:** Greedy / Array

## Problem Description
There are `n` gas stations along a circular route, where the amount of gas at the `ith` station is `gas[i]`.

You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from the `ith` station to its next `(i + 1)th` station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays `gas` and `cost`, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return `-1`. If there exists a solution, it is **guaranteed to be unique**.
---
**Example 1:**
```text
Input: gas = [1,2,3,4], cost = [2,2,4,1]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 1 + 1 = 4
Travel to station 1. Your tank = 4 - 2 + 2 = 4
Travel to station 2. Your tank = 4 - 2 + 3 = 5
Travel to station 3. The cost is 4. Your tank = 5 - 4 = 1
The circuit is complete, so return 3.
```

```text
Input: gas = [1,2,3], cost = [2,3,2]
Output: -1
Explanation:
You cannot start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 3 units of gas. Your tank = 0 + 3 = 3
Travel to station 0. Your tank = 3 - 2 + 1 = 2
Travel to station 1. Your tank = 2 - 2 + 2 = 2
You cannot travel back to station 2, as it requires 3 units of gas but you only have 2.
Therefore, you can't travel around the circuit once no matter where you start.
```
---
**Constraints:**
* `1 <= gas.length == cost.length <= 100000`
* `0 <= gas[i], cost[i] <= 1000`
---
## Complexity Analysis
* **Time Complexity:** $\mathcal{O}(n)$ where $n$ is the number of stations. We iterate through the arrays exactly once.
* **Space Complexity:**  $\mathcal{O}(1)$ because we only use a few integer variables (total_gas, current_gas, and start_index) to track the running totals.

---
## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest test_solution.py -v`
```