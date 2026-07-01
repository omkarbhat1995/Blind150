class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Checks if s2 contains a permutation of s1 as a substring.
        
        :param s1: The string to find a permutation of.
        :param s2: The string to search within.
        :return: True if a permutation is found, False otherwise.
        """
        len1, len2 = len(s1), len(s2)
        
        # If s1 is longer than s2, it is impossible for s2 to contain a permutation of s1
        if len1 > len2:
            return False
            
        s1_count = [0] * 26
        window_count = [0] * 26
        
        # Populate the initial frequency map for s1 and the first window in s2
        for i in range(len1):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1
            
        # Check if the very first window is a match
        if s1_count == window_count:
            return True
            
        # Slide the window across the rest of s2
        for i in range(len1, len2):
            # Add the new character entering the window on the right
            window_count[ord(s2[i]) - ord('a')] += 1
            
            # Remove the old character that is left behind
            window_count[ord(s2[i - len1]) - ord('a')] -= 1
            
            # Check for a match
            if s1_count == window_count:
                return True
                
        return False