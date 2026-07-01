from typing import Dict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Finds the minimum window substring of s that contains all characters of t.
        
        :param s: The string to search within.
        :param t: The target characters to find.
        :return: The shortest valid substring, or an empty string if none exists.
        """
        if not t or not s:
            return ""

        # Map to track the frequencies of characters required
        count_t: Dict[str, int] = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        window: Dict[str, int] = {}
        have, need = 0, len(count_t)
        
        # res stores [left_index, right_index], res_len tracks the shortest length
        res, res_len = [-1, -1], float('infinity')
        left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            # If the current character is in target and its frequency matches the requirement
            if char in count_t and window[char] == count_t[char]:
                have += 1

            # Shrink the window from the left as long as the window remains valid
            while have == need:
                # Update the smallest window bounds
                current_window_size = right - left + 1
                if current_window_size < res_len:
                    res = [left, right]
                    res_len = current_window_size

                # Pop the leftmost character from our window
                left_char = s[left]
                window[left_char] -= 1
                
                # If popping the character breaks our requirement, update the 'have' variable
                if left_char in count_t and window[left_char] < count_t[left_char]:
                    have -= 1
                    
                left += 1

        l, r = res
        return s[l:r+1] if res_len != float('infinity') else ""