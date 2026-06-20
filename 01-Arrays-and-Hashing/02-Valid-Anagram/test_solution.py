import pytest
from solution import Solution

class TestValidAnagram:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.solver = Solution()

    @pytest.mark.parametrize("s, t, expected", [
        # --- Standard LeetCode Examples ---
        ("racecar", "carrace", True),                                
        ("jar", "jam", False),                                       
        ("anagram", "nagaram", True),                                
        
        # --- Length Edge Cases ---
        ("a", "a", True),                                            
        ("a", "b", False),                                           
        ("ab", "a", False),                                          
        ("a", "ab", False),                                          
        
        # --- Structural & Alphabet Edge Cases ---
        ("abcdefghijklmnopqrstuvwxyz", 
         "zyxwvutsrqponmlkjihgfedcba", True),                        
        ("aabbcc", "abcabc", True),                                  
        ("aabbcc", "aabbcd", False),                                 
        ("bbcc", "cbce", False),                                     
        ("hello", "ollhe", True)                                     
    ])
    def test_isAnagram(self, s, t, expected):
        assert self.solver.isAnagram(s, t) == expected

    # --- Isolated Constraint Edge Cases ---
    # We test the 50,000 character limits in a dedicated function 
    # so Pytest doesn't crash the Windows terminal trying to print them.
    def test_isAnagram_max_constraints_true(self):
        s = "a" * 50000
        t = "a" * 50000
        assert self.solver.isAnagram(s, t) == True

    def test_isAnagram_max_constraints_false(self):
        s = "a" * 50000
        t = "b" * 50000
        assert self.solver.isAnagram(s, t) == False

    def test_isAnagram_max_constraints_mixed(self):
        s = "a" * 49999 + "b"
        t = "b" + "a" * 49999
        assert self.solver.isAnagram(s, t) == True