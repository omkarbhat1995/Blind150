
"""
Problem: Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/
Approach: Use a Hash Map where the key is a tuple representing the character count 
(26 zeroes for a-z) and the value is a list of strings that match that count.
Time Complexity: O(m * n) where m is number of strings, n is average length
Space Complexity: O(m * n)
"""
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map a character count tuple to a list of anagrams
        ans = defaultdict(list)
        
        for s in strs:
            # Initialize an array of 26 zeroes
            count = [0] * 26
        
            # Count the frequency of each character
            for c in s.lower():
                count[ord(c) - ord('a')] += 1
                
            # Convert the list to a tuple so it can be hashed as a dictionary key
            ans[tuple(count)].append(s)
        print(ans)    
        return list(ans.values())
