import pytest
from solution import Solution

sol = Solution()

def normalize(words):
    """
    Sorts the output list to ensure order-agnostic comparison.
    Because the problem states 'return all words that are present' in any order.
    """
    return sorted(words)

@pytest.mark.parametrize("board, words, expected", [
    # --- 1. Standard LeetCode Examples ---
    (
        [["a","b","c","d"], ["s","a","a","t"], ["a","c","k","e"], ["a","c","d","n"]], 
        ["bat","cat","back","backend","stack"], 
        ["back","backend","cat"]
    ),
    (
        [["x","o"], ["x","o"]], 
        ["xoxo"], 
        []
    ),

    # --- 2. Single Cell Constraints ---
    ([["a"]], ["a"], ["a"]),                                            # Exact match
    ([["a"]], ["b"], []),                                               # No match
    ([["a"]], ["a", "aa"], ["a"]),                                      # Overly long word filtered

    # --- 3. Full Board Same Character ---
    (
        [["a","a"], ["a","a"]], 
        ["a", "aa", "aaa", "aaaa", "aaaaa"], 
        ["a", "aa", "aaa", "aaaa"]                                      # Max length constrained by board size
    ),

    # --- 4. Sub-words & Prefixes ---
    (
        [["c","a","r","t"]], 
        ["c", "car", "cart", "art"], 
        ["c", "car", "cart", "art"]                                     # "art" is valid at the end
    ),

    # --- 5. No Words Present ---
    (
        [["q","w"], ["e","r"]], 
        ["z", "zx", "zxc"], 
        []
    ),

    # --- 6. Zig-Zag Traversals ---
    (
        [["z","i","g"], ["g","a","z"], ["g","z","i"]], 
        ["zigzag"], 
        ["zigzag"]
    ),

    # --- 7. Reusing Cells Trap (Should Fail) ---
    (
        [["a","b"]], 
        ["aba"], 
        []                                                              # Cannot reuse 'a'
    ),

    # --- 8. Dead Ends / Backtracking Check ---
    (
        [["a","b","c"], ["d","e","f"], ["g","h","i"]], 
        ["abcf", "abce", "abfe"], 
        ["abcf"]                                                        # "abce" requires an invalid diagonal jump
    ),

    # --- 9. Multiple Words Originating from Same Cell ---
    (
        [["o","a","a","n"], ["e","t","a","e"], ["i","h","k","r"], ["i","f","l","v"]], 
        ["oath","pea","eat","rain"], 
        ["eat","oath"]
    ),

    # --- 10. Max Length Word ---
    (
        [["a","b","c"], ["d","e","f"], ["g","h","i"]], 
        ["abcdefghi", "adghebcfi"], 
        ["adghebcfi"]                                                   # Requires strict winding path
    ),

    # --- 11. Surrounding Box Traversal ---
    (
        [["b","o","x"], ["e","o","e"], ["b","o","x"]], 
        ["boxeboxb", "box", "oxe"], 
        ["box", "oxe"]                                                  # "boxeboxb" cannot be completed legally
    ),

    # --- 12. Multiple Disconnected Starts for Same Word ---
    (
        [["h","i","x"], ["x","x","x"], ["h","i","x"]], 
        ["hi"], 
        ["hi"]                                                          # Exists twice, but only returned once
    ),

    # --- 13. Complex Overlap ---
    (
        [["m","b","c"], ["a","p","p"], ["l","e","e"]], 
        ["map", "apple", "app", "bce"], 
        ["app", "map"]                                                  # "apple" and "bce" require illegal jumps
    ),

    # --- 14. Deeply Nested Non-Existent Words ---
    (
        [["t","e","s","t"]], 
        ["tester", "testing", "testify"], 
        []
    ),

    # --- 15. Board with Diagonals Allowed Trap ---
    (
        [["a","b"], ["c","d"]], 
        ["ad", "cb"], 
        []                                                              # Diagonal paths are strictly forbidden
    )
])
def test_findWords(board, words, expected):
    """
    Tests the findWords Trie/DFS logic against 15 distinct boundary, edge, and standard cases.
    """
    assert normalize(sol.findWords(board, words)) == normalize(expected)