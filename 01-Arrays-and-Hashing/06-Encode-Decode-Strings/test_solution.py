import pytest
from solution import Solution

class TestEncodeDecode:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.solver = Solution()

    @pytest.mark.parametrize("strs", [
        # --- Standard Examples ---
        (["Hello", "World"]),
        (["neetcode", "is", "awesome"]),
        
        # --- Empty and Null-like Cases ---
        ([]),                                          # Empty list
        ([""]),                                        # List with one empty string
        (["", "", ""]),                                # List with multiple empty strings
        
        # --- Delimiter and Number Edge Cases (The "Gotchas") ---
        (["#", "##", "###"]),                          # Strings that are just the delimiter
        (["5#Hello", "3#a", "10#", "##"]),             # Strings that mimic the encoding logic
        (["12345", "67890"]),                          # Strings that are just numbers
        (["a#b#c", "d#e#f"]),                          # Delimiters mixed inside text
        
        # --- Special Character and Spacing Edge Cases ---
        ([" ", "   ", " "]),                           # Spaces
        (["\n", "\t", "\r"]),                          # Escape characters
        (["!@$%^&*()_+", "{}[];':\",.<>/?`~"]),        # Special ASCII characters
        
        # --- Structural Edge Cases ---
        (["a", "b", "c", "d", "e", "f", "g"]),         # Many single characters
        (["a" * 150, "b" * 150])                       # Longer string blocks
    ])
    def test_encode_decode(self, strs):
        # The ultimate test: Encoding and then Decoding should return the exact original input
        encoded = self.solver.encode(strs)
        decoded = self.solver.decode(encoded)
        assert decoded == strs

    # --- Isolated Constraint Edge Cases ---
    
    def test_encode_decode_max_constraints(self):
        # Constraint max: 100 strings, each 200 characters long
        strs = ["a" * 199 for _ in range(99)]
        
        encoded = self.solver.encode(strs)
        decoded = self.solver.decode(encoded)
        
        assert decoded == strs