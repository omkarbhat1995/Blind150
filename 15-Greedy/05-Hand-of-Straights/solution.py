import heapq
from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        Determines if the hand of cards can be cleanly divided into groups of `groupSize` 
        consisting of consecutive integers.
        """
        # A valid grouping is mathematically impossible if the total number of cards 
        # is not perfectly divisible by the group size.
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        
        # Use a Min-Heap of the unique card values to always process the smallest available card first
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0]
            
            # Form a sequence of length `groupSize` starting from the smallest available card
            for i in range(first, first + groupSize):
                if count[i] == 0:
                    return False
                
                count[i] -= 1
                
                # If a card count drops to 0, it MUST be the smallest card currently in the heap.
                # If a larger card runs out before the smallest card, a valid sequence is broken.
                if count[i] == 0:
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
                    
        return True