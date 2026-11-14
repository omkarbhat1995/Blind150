# Find Median From Data Stream

**Difficulty:** Hard
**Category:** Heap / Priority Queue

## Problem Description
The median is the middle value in a sorted list of integers. For lists of even length, there is no middle value, so the median is the mean of the two middle values.
* For example, for `arr = [1,2,3]`, the median is `2`.
* For example, for `arr = [1,2]`, the median is `(1 + 2) / 2 = 1.5`.

Implement the `MedianFinder` class:
* `MedianFinder()` initializes the `MedianFinder` object.
* `void addNum(int num)` adds the integer `num` from the data stream to the data structure.
* `double findMedian()` returns the median of all elements so far.

**Example 1:**
```text
Input:
["MedianFinder", "addNum", "1", "findMedian", "addNum", "3", "findMedian", "addNum", "2", "findMedian"]
Output:
[null, null, 1.0, null, 2.0, null, 2.0]

Explanation:
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.findMedian(); // return 1.0
medianFinder.addNum(3);    // arr = [1, 3]
medianFinder.findMedian(); // return 2.0
medianFinder.addNum(2);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

Complexity Analysis   

### Time Complexity:
    *addNum: $O(\log n)$ to push and pop from the heaps.
    *findMedian: $O(1)$ to retrieve the root of the heaps.
### Space Complexity: $O(n)$ to store all numbers from the data stream in the heaps.