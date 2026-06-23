
"""
Problem: Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/
Approach: Use a fixed-size frequency array of 26 buckets (for lowercase English letters) 
to count character occurrences. Increment for string `s`, decrement for string `t`.
Time Complexity: O(n + m)
Space Complexity: O(1)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the strings are different lengths, they cannot be anagrams
        s,t= s.lower(), t.lower()
        if len(s) != len(t):
            return False
            
        # Initialize a fixed array of 26 zeroes
        char_counts = [0] * 26
        
        # Increment for characters in s, decrement for characters in t
        for i in range(len(s)):
            char_counts[ord(s[i]) - ord('a')] += 1
            char_counts[ord(t[i]) - ord('a')] -= 1
            
        # If any bucket is not zero, there is a character imbalance
        for count in char_counts:
            if count != 0:
                return False
                
        return True