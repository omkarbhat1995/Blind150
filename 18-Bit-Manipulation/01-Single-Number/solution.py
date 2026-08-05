from typing import List

class Solution:
    """
    Optimal O(n) time and O(1) space solution using Bitwise XOR.
    """
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            # XOR the current number with our running result
            res ^= n
        return res