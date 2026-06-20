"""
Problem: Encode and Decode Strings
Link: https://leetcode.com/problems/encode-and-decode-strings/ (Premium)
Approach: Length-Prefix Encoding. Format each string as `length + "#" + string`.
During decoding, read the integer before the `#` to know exactly how many 
characters to extract, preventing issues with special characters in the string.
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Append the length of the string, a delimiter, and the string itself
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        
        while i < len(s):
            j = i
            # Find the delimiter to isolate the length integer
            while s[j] != "#":
                j += 1
                
            length = int(s[i:j])
            
            # Extract the actual string using the parsed length
            # s[j+1] is the start of the string, j+1+length is the end
            res.append(s[j + 1 : j + 1 + length])
            
            # Move the pointer to the start of the next encoded string
            i = j + 1 + length
            
        return res