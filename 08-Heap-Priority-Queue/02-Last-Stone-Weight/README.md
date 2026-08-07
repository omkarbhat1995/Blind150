# Last Stone Weight

## Problem Description
You are given an array of integers `stones` where `stones[i]` represents the weight of the `i`th stone.

We want to run a simulation on the stones as follows:
* At each step, we choose the **two heaviest stones** and smash them together. Suppose the stones have weights `x` and `y` with `x <= y`.
* If `x == y`, both stones are destroyed.
* If `x < y`, the stone of weight `x` is destroyed, and the stone of weight `y` has a new weight of `y - x`.

Continue the simulation until there is no more than one stone remaining. Return the weight of the last remaining stone, or return `0` if no stones remain.

## Approach
The most optimal way to repeatedly find the two largest elements in a dynamic dataset is to use a **Max-Heap** (Priority Queue).
1. Python's `heapq` library only implements a Min-Heap. To simulate a Max-Heap, we can negate all the values in the `stones` array.
2. We transform the array into a heap in-place in `O(n)` time.
3. While there is more than one stone in the heap, we pop the two smallest (which are the most negative, hence the heaviest).
4. If their weights differ, we push the difference (again, as a negative number) back into the heap.
5. If the heap is empty at the end, we return `0`. Otherwise, we return the absolute value of the remaining element.

## Complexity Analysis
* **Time Complexity:** * `O(n)` to initialize the heap.
  * `O(n log n)` to process the stones, as we do at most `n - 1` operations, and each push/pop takes `O(log n)`.
  * **Overall Time Complexity:** `O(n log n)`
* **Space Complexity:** `O(n)` or `O(1)` depending on whether we modify the input array in-place or create a new one. In Python, mutating the input array gives us `O(1)` auxiliary space, though strictly speaking, the heap itself conceptually holds `n` elements.