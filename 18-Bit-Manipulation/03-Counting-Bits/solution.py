from typing import List
class Solution:
    """
    Optimal O(1) time and space solution using the n & (n - 1) bitwise trick 
    to continuously flip the least-significant 1-bit to 0.
    """
    def hammingWeight(self,n:int)-> int:
        count=0
        while n:
            n&=(n-1)
            count+=1
        return count
    
    def countBits(self, n: int) -> List[int]:
        count = []
        for i in range(n + 1):
            count.append(self.hammingWeight(i))
        return count
        