# Car Fleet

## Problem Description
There are `n` cars traveling to the same destination on a one-lane highway. You are given two arrays of integers `position` and `speed`, both of length `n`.

- `position[i]` is the position of the `ith` car (in miles).
- `speed[i]` is the speed of the `ith` car (in miles per hour).
- The destination is at position `target` miles.

A car cannot pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it. A **car fleet** is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

If a car catches up to a car fleet at the exact moment the fleet reaches the destination, it is considered part of the fleet.

Return the number of different car fleets that will arrive at the destination.

**Constraints:**
- `n == position.length == speed.length`
- `1 <= n <= 1000`
- `0 < target <= 1000`
- `0 < speed[i] <= 100`
- `0 <= position[i] < target`
- All the values of `position` are unique.

## Approach: Sorting and Stack
To determine if a car will catch up to the car ahead of it, we need to calculate the time it takes for each car to reach the destination: `time = (target - position) / speed`.

1. We pair each car's position with its speed and sort the array in **descending order** by position (closest to the target first).
2. We iterate through the sorted cars and calculate their time to reach the target, pushing this time onto a stack.
3. If the stack has at least two cars, we compare the top two. If the car behind (top of the stack) has a time **less than or equal to** the car ahead (second to top), it means the car behind will catch up.
4. Because they form a fleet, the car behind will match the speed of the car ahead. We handle this by simply popping the faster car's time off the stack, effectively merging them.
5. In the end, the length of the stack represents the number of distinct fleets.

## Complexity
- **Time Complexity:** O(n log n) - Sorting the array of cars takes O(n log n) time. The subsequent stack iteration takes exactly O(n) time.
- **Space Complexity:** O(n) - We allocate O(n) space to store the pairs of positions and speeds, as well as O(n) space for the stack.