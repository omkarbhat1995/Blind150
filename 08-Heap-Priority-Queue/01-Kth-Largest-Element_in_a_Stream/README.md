# Kth Largest Element in a Stream

## Problem Description
Design a class to find the `k`th largest integer in a stream of values, including duplicates. The stream is not necessarily sorted.

Implement the `KthLargest` class:
* `KthLargest(int k, int[] nums)`: Initializes the object with the integer `k` and the stream of integers `nums`.
* `int add(int val)`: Adds the integer `val` to the stream and returns the `k`th largest integer.

## Approach
The optimal way to solve this is by using a **Min-Heap**.
1. We initialize a Min-Heap with the elements of `nums`.
2. To keep track of only the `k` largest elements, we pop elements from the heap until its size is exactly `k`. The smallest element in this heap of size `k` (which sits at the root) is our `k`th largest element overall.
3. When `add(val)` is called, we push the new value onto the heap. If the heap size exceeds `k`, we pop the smallest element. 
4. We then return the root of the heap.

## Complexity Analysis
* **Time Complexity:** * Initialization: $O(n \log k)$ where $n$ is the length of `nums`. (Or $O(n \log n)$ if we heapify all elements and then pop down to $k$). Using `heapq.heapify()` takes $O(n)$, and popping down to `k` takes $O((n - k) \log k)$.
  * `add(val)`: $O(\log k)$ because the heap size is strictly maintained at `k`.
* **Space Complexity:** $O(k)$ to store the `k` largest elements in the heap.