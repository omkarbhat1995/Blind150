import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right
        
        while left <= right:
            k = left + (right - left) // 2
            
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
                
            if hours <= h:
                res = min(res, k)
                # Try to find an even smaller valid speed
                right = k - 1
            else:
                # Eating too slow, need to increase speed
                left = k + 1
                
        return res