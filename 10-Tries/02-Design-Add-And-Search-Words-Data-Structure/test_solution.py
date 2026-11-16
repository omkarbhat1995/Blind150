import pytest
from solution import WordDictionary

@pytest.mark.parametrize("commands, args, expected", [
    # 1. Standard LeetCode Example
    (
        ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"],
        [[], ["day"], ["bay"], ["may"], ["say"], ["day"], [".ay"], ["b.."]],
        [None, None, None, None, False, True, True, True]
    ),

    # 2. Search exact match vs Prefix trap
    (
        ["WordDictionary", "addWord", "search", "search"],
        [[], ["hello"], ["hello"], ["hell"]],
        [None, None, True, False]
    ),

    # 3. Single character insertions and lookups
    (
        ["WordDictionary", "addWord", "search", "search", "search"],
        [[], ["a"], ["a"], ["."], ["b"]],
        [None, None, True, True, False]
    ),

    # 4. Search word longer than any added word
    (
        ["WordDictionary", "addWord", "search", "search"],
        [[], ["car"], ["cart"], ["car."]],
        [None, None, False, False]
    ),

    # 5. Pure wildcard lookups of varying lengths
    (
        ["WordDictionary", "addWord", "addWord", "search", "search", "search"],
        [[], ["ab"], ["abc"], ["."], [".."], ["..."]],
        [None, None, None, False, True, True]
    ),

    # 6. Maximum allowed dots (2 dots)
    (
        ["WordDictionary", "addWord", "addWord", "search", "search", "search"],
        [[], ["cat"], ["bat"], ["c.t"], [".a."], ["..t"]],
        [None, None, None, True, True, True]
    ),

    # 7. Disjoint words with similar endings
    (
        ["WordDictionary", "addWord", "addWord", "search", "search"],
        [[], ["testing"], ["rusting"], ["r.sting"], ["t.sting"]],
        [None, None, None, True, True]
    ),

    # 8. Re-inserting the exact same word
    (
        ["WordDictionary", "addWord", "addWord", "search", "search"],
        [[], ["duplicate"], ["duplicate"], ["duplicate"], ["d.plicat."]],
        [None, None, None, True, True]
    ),

    # 9. Wildcard fails early on deep Trie
    (
        ["WordDictionary", "addWord", "addWord", "search"],
        [[], ["python"], ["java"], ["p.th.m"]],
        [None, None, None, False]
    ),

    # 10. Empty Trie Search
    (
        ["WordDictionary", "search", "search"],
        [[], ["a"], ["."]],
        [None, False, False]
    ),

    # 11. Overlapping words forming a deep branch
    (
        ["WordDictionary", "addWord", "addWord", "addWord", "search", "search"],
        [[], ["app"], ["apple"], ["apply"], ["appl."], ["app.."]],
        [None, None, None, None, True, True]
    ),

    # 12. Alternating adds and searches
    (
        ["WordDictionary", "addWord", "search", "addWord", "search", "search"],
        [[], ["a"], ["."], ["ab"], [".."], ["a."]],
        [None, None, True, None, True, True]
    ),

    # 13. Dot prefix resolving to different paths
    (
        ["WordDictionary", "addWord", "addWord", "addWord", "search"],
        [[], ["ran"], ["run"], ["ruin"], [".un"]],
        [None, None, None, None, True]
    ),

    # 14. Completely disjoint paths with dot searches
    (
        ["WordDictionary", "addWord", "addWord", "addWord", "search", "search"],
        [[], ["abc"], ["def"], ["ghi"], ["a.c"], ["d.f"]],
        [None, None, None, None, True, True]
    ),

    # 15. The "Missed by One Character" Boundary Trap
    (
        ["WordDictionary", "addWord", "search", "search", "search"],
        [[], ["abcdefghijklmnopqrstuvwxyz"], ["abcdefghijklmnopqrstuvwxy."], [".bcdefghijklmnopqrstuvwxyz"], ["abcdefghijklmnopqrstuvwxy"]],
        [None, None, True, True, False]
    )
])
def test_word_dictionary(commands, args, expected):
    """
    Tests the WordDictionary class using a sequence of commands and arguments.
    """
    obj = None
    results = []
    
    for cmd, arg in zip(commands, args):
        if cmd == "WordDictionary":
            obj = WordDictionary()
            results.append(None)
        elif cmd == "addWord" and obj is not None:
            obj.addWord(arg[0])
            results.append(None)
        elif cmd == "search" and obj is not None:
            results.append(obj.search(arg[0]))
            
    assert results == expected