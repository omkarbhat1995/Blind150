class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.
        
        :param s: The input string consisting of printable ASCII characters.
        :return: The length of the longest valid substring.
        """
        char_map = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            current_char = s[right]
            
            # If the character is in our map and its recorded index is within our current window
            if current_char in char_map and char_map[current_char] >= left:
                # Shrink the window by moving the left pointer past the duplicate
                left = char_map[current_char] + 1
                
            # Update the latest index of the current character
            char_map[current_char] = right
            
            # Calculate the current window length and update max_length if necessary
            current_window_length = right - left + 1
            if current_window_length > max_length:
                max_length = current_window_length
                
        return max_length