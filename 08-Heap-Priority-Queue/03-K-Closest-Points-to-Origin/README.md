# K Closest Points to Origin

## Problem Description
You are given a 2-D array `points` where `points[i] = [xi, yi]` represents the coordinates of a point on an X-Y axis plane. You are also given an integer `k`.

Return the `k` closest points to the origin `(0, 0)`.
The distance between two points is defined as the Euclidean distance ($\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order in which the points are returned).

## Approach
The optimal approach for finding the "top K" or "minimum K" elements in a dataset is to use a **Max-Heap**.
1. **Distance Optimization:** Computing the actual Euclidean distance requires taking a square root, which is computationally expensive and can lead to floating-point precision issues. Since we only need relative comparisons, we can just compare the squared distances: $x^2 + y^2$.
2. **Max-Heap Simulation:** Python's `heapq` module only implements a Min-Heap. To keep track of the *closest* points, we need a Max-Heap of size `k` to easily pop off the *farthest* points when our heap exceeds size `k`. We simulate this by pushing the negative of the squared distance.
3. **Execution:** We iterate through the points, pushing `(-squared_distance, x, y)` onto the heap. If the heap size exceeds `k`, we pop the top element (which, because it's negated, is the largest distance).
4. Finally, we extract the remaining `x` and `y` coordinates from the heap and return them.

## Complexity Analysis
* **Time Complexity:** $O(N \log k)$, where $N$ is the total number of points. We iterate through $N$ points, and pushing/popping from a heap of size $k$ takes $O(\log k)$ time.
* **Space Complexity:** $O(k)$ to store the `k` closest points in our heap.