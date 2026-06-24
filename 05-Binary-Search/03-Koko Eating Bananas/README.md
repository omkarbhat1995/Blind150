# Koko Eating Bananas

## Problem Description
You are given an integer array `piles` where `piles[i]` is the number of bananas in the `ith` pile. You are also given an integer `h`, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of `k`. Each hour, you may choose a pile of bananas and eat `k` bananas from that pile. If the pile has less than `k` bananas, you may finish eating the pile but you cannot eat from another pile in the same hour.

Return the minimum integer `k` such that you can eat all the bananas within `h` hours.

**Constraints:**
- `1 <= piles.length <= 1000`
- `piles.length <= h <= 1,000,000`
- `1 <= piles[i] <= 1,000,000,000`

## Approach: Binary Search on Answer
Instead of iterating `k` from 1 upwards to find the minimum speed (which would take $O(\text{max}(piles) \times \text{length of piles})$ and result in a Time Limit Exceeded error), we can use **Binary Search**.

1. **Define the Search Space:** The minimum possible eating speed is `1` banana per hour. The maximum speed we ever need to consider is `max(piles)` because eating faster than the largest pile still takes 1 hour per pile.
2. **Binary Search:** We set our pointers: `left = 1` and `right = max(piles)`. We calculate the midpoint `mid` to test as our potential eating rate `k`.
3. **Validation:** For a given `k`, we calculate the total hours required to eat all piles using `math.ceil(pile / k)`. 
4. **Adjust Pointers:** - If the total hours $\le h$, this `k` is valid, but we might be able to eat even slower. We record this `k` and search the left half (`right = mid - 1`).
   - If the total hours $> h$, Koko is eating too slowly. We must increase the speed, so we search the right half (`left = mid + 1`).

## Complexity
- **Time Complexity:** $O(N \log M)$ where $N$ is the length of the `piles` array and $M$ is the maximum value in `piles`. We iterate through the array $O(N)$ for every step of our binary search $O(\log M)$.
- **Space Complexity:** $O(1)$ since we are only using a few variables for pointers and calculations.