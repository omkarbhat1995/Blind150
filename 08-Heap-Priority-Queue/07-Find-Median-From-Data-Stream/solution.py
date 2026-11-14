import heapq

class MedianFinder:
    def __init__(self):
        """
        Initializes the MedianFinder object using two heaps.
        small: Max-Heap storing the smaller half of the numbers.
        large: Min-Heap storing the larger half of the numbers.
        """
        self.small = []  # Max-Heap (requires negation trick)
        self.large = []  # Min-Heap

    def addNum(self, num: int) -> None:
        """
        Adds num into the data structure while maintaining heap balance.
        """
        # Python's heapq only supports Min-Heaps out of the box[cite: 1]. 
        # To simulate a Max-Heap, multiply numerical values by -1 before pushing them[cite: 1].
        heapq.heappush(self.small, -num)

        # Ensure every element in small is <= every element in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance the sizes so small is either equal to or exactly 1 element larger than large
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        """
        Returns the median of all elements so far.
        """
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0