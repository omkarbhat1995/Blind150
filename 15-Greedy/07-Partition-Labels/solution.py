from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        Partitions a string into as many substrings as possible such that 
        each letter appears in at most one substring.
        Uses a Greedy approach by finding the furthest last occurrence of characters 
        in the current window.
        """
        # Record the exact last index of every character in the string
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        partitions = []
        start, end = 0, 0
        
        for i, char in enumerate(s):
            # Continuously push the end of the partition outward if a character 
            # appears later in the string
            end = max(end, last_occurrence[char])
            
            # When our current index catches up to the furthest boundary, 
            # the partition is safely closed
            if i == end:
                partitions.append(end - start + 1)
                start = i + 1
                
        return partitions