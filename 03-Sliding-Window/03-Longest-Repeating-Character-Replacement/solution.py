from typing import Dict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Finds the longest substring with the same character after at most k replacements.
        
        :param s: The input string consisting of uppercase English letters.
        :param k: The maximum number of replacements allowed.
        :return: The length of the longest valid substring.
        """
        count: Dict[str, int] = {}
        max_length = 0
        left = 0
        max_frequency = 0
        
        for right in range(len(s)):
            current_char = s[right]
            count[current_char] = count.get(current_char, 0) + 1
            
            # Keep track of the highest frequency of a single character in the current window
            max_frequency = max(max_frequency, count[current_char])
            
            # The number of characters to replace is the window length minus the max_frequency.
            # If this exceeds k, the window is invalid and we must shrink it from the left.
            current_window_length = right - left + 1
            if current_window_length - max_frequency > k:
                count[s[left]] -= 1
                left += 1
                
            # Update the max_length. We calculate the valid window size as (right - left + 1)
            # because the window length is only updated when a valid state is maintained or expanded.
            max_length = max(max_length, right - left + 1)
            
        return max_length