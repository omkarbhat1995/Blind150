import pytest
from solution import PrefixTree

@pytest.mark.parametrize("commands, args, expected", [
    # --- 1. Standard LeetCode Example ---
    (
        ["PrefixTree", "insert", "search", "search", "startsWith", "insert", "search"],
        [[], ["dog"], ["dog"], ["do"], ["do"], ["do"], ["do"]],
        [None, None, True, False, True, None, True]
    ),

    # --- 2. Single Character Edges ---
    (
        ["PrefixTree", "insert", "search", "startsWith", "search"],
        [[], ["a"], ["a"], ["a"], ["b"]],
        [None, None, True, True, False]
    ),

    # --- 3. Deep Hierarchy (Overlapping Words) ---
    (
        ["PrefixTree", "insert", "insert", "search", "search", "startsWith"],
        [[], ["apple"], ["app"], ["app"], ["apple"], ["appl"]],
        [None, None, None, True, True, True]
    ),

    # --- 4. Search for Word Longer Than Inserted ---
    (
        ["PrefixTree", "insert", "search", "startsWith"],
        [[], ["car"], ["cart"], ["cart"]],
        [None, None, False, False]
    ),

    # --- 5. Completely Disjoint Words ---
    (
        ["PrefixTree", "insert", "insert", "insert", "search", "search", "startsWith"],
        [[], ["cat"], ["dog"], ["bat"], ["cat"], ["bat"], ["d"]],
        [None, None, None, None, True, True, True]
    ),

    # --- 6. Identical Character Chains ---
    (
        ["PrefixTree", "insert", "search", "startsWith", "search"],
        [[], ["aaaa"], ["aaa"], ["aaa"], ["aaaa"]],
        [None, None, False, True, True]
    ),

    # --- 7. Exact Match vs Prefix ---
    (
        ["PrefixTree", "insert", "startsWith", "search"],
        [[], ["hello"], ["hello"], ["hello"]],
        [None, None, True, True]
    ),

    # --- 8. Re-inserting the Same Word ---
    (
        ["PrefixTree", "insert", "insert", "search"],
        [[], ["test"], ["test"], ["test"]],
        [None, None, None, True]
    ),

    # --- 9. Fails Early on First Character ---
    (
        ["PrefixTree", "insert", "search", "startsWith"],
        [[], ["python"], ["java"], ["j"]],
        [None, None, False, False]
    ),

    # --- 10. Heavy Alternating Operations ---
    (
        ["PrefixTree", "startsWith", "insert", "search", "insert", "startsWith", "search"],
        [[], ["a"], ["a"], ["a"], ["ab"], ["ab"], ["ab"]],
        [None, False, None, True, None, True, True]
    ),

    # --- 11. Large Word Constraints (Boundary Simulator) ---
    (
        ["PrefixTree", "insert", "search", "startsWith", "search"],
        [[], ["z" * 1000], ["z" * 1000], ["z" * 999], ["z" * 1001]],
        [None, None, True, True, False]
    ),

    # --- 12. Diverging Branches at Root ---
    (
        ["PrefixTree", "insert", "insert", "insert", "search", "search", "search"],
        [[], ["abc"], ["def"], ["ghi"], ["abc"], ["def"], ["ghi"]],
        [None, None, None, None, True, True, True]
    ),

    # --- 13. Case/Character Specificity (Lowercase alphabet bounds) ---
    (
        ["PrefixTree", "insert", "search", "startsWith"],
        [[], ["abcdefghijklmnopqrstuvwxyz"], ["abcdefghijklmnopqrstuvwxyz"], ["abcdefg"]],
        [None, None, True, True]
    ),

    # --- 14. Missing Middle Character ---
    (
        ["PrefixTree", "insert", "search", "startsWith"],
        [[], ["testing"], ["tesing"], ["tesi"]],
        [None, None, False, False]
    ),

    # --- 15. The "Word is a Prefix of Another" Trap ---
    (
        ["PrefixTree", "insert", "insert", "search", "startsWith", "search"],
        [[], ["interstellar"], ["internet"], ["inter"], ["intern"], ["internet"]],
        [None, None, None, False, True, True]
    )
])
def test_prefix_tree(commands, args, expected):
    """
    Tests the PrefixTree class using a sequence of commands and arguments.
    """
    obj = None
    results = []
    
    for cmd, arg in zip(commands, args):
        if cmd in ("PrefixTree", "Trie"):
            obj = PrefixTree()
            results.append(None)
        elif cmd == "insert" and obj is not None:
            results.append(obj.insert(arg[0]))
        elif cmd == "search" and obj is not None:
            results.append(obj.search(arg[0]))
        elif cmd == "startsWith" and obj is not None:
            results.append(obj.startsWith(arg[0]))
            
    assert results == expected