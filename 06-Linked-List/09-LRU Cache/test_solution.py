import pytest
from solution import LRUCache

@pytest.mark.parametrize("commands, args, expected", [
    # Standard Examples
    (
        ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
        [None, None, None, 1, None, -1, None, -1, 3, 4]
    ),
    (
        ["LRUCache", "put", "get", "put", "put", "get", "get"],
        [[2], [1, 10], [1], [2, 20], [3, 30], [2], [1]],
        [None, None, 10, None, None, 20, -1]
    ),
    
    # Capacity Constraints
    (
        ["LRUCache", "put", "get", "put", "get"],
        [[1], [1, 1], [1], [2, 2], [1]],
        [None, None, 1, None, -1] # Capacity 1 immediately evicts
    ),
    (
        ["LRUCache", "put", "put", "put", "put", "get"],
        [[3], [1, 10], [2, 20], [3, 30], [4, 40], [1]],
        [None, None, None, None, None, -1] # Flat overflow
    ),
    
    # Updating Existing Keys (Does not increase capacity)
    (
        ["LRUCache", "put", "put", "put", "get"],
        [[2], [2, 1], [2, 2], [2, 3], [2]],
        [None, None, None, None, 3] # Overwriting same key updates MRU
    ),
    (
        ["LRUCache", "put", "put", "get", "put", "put", "get"],
        [[2], [2, 1], [1, 1], [2], [1, 4], [2, 2], [1]],
        [None, None, None, 1, None, None, 4] 
    ),
    
    # Missing / Non-existent Key Checks
    (
        ["LRUCache", "get", "get", "put", "get"],
        [[2], [10], [100], [1, 5], [2]],
        [None, -1, -1, None, -1] 
    ),
    
    # High Frequency Ping-Pong
    (
        ["LRUCache", "put", "put", "get", "get", "get", "get"],
        [[2], [1, 10], [2, 20], [1], [2], [1], [2]],
        [None, None, None, 10, 20, 10, 20] 
    ),

    # Rapid Capacity Cycling
    (
        ["LRUCache", "put", "put", "put", "put", "put", "get"],
        [[1], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [4]],
        [None, None, None, None, None, None, -1] 
    ),
    
    # Large Number Keys/Values (Constraints Check)
    (
        ["LRUCache", "put", "put", "get"],
        [[5], [1000, 1000], [0, 0], [1000]],
        [None, None, None, 1000]
    ),
    
    # Eviction due to put followed immediately by get checking eviction
    (
        ["LRUCache", "put", "put", "put", "get", "get", "get"],
        [[2], [1, 10], [2, 20], [3, 30], [1], [2], [3]],
        [None, None, None, None, -1, 20, 30]
    ),

    # Overwrite evicts oldest properly
    (
        ["LRUCache", "put", "put", "put", "put", "get", "get"],
        [[2], [1, 10], [2, 20], [1, 15], [3, 30], [2], [1]],
        [None, None, None, None, None, -1, 15]
    ),
    
    # Capacity boundary edge (cap=100)
    (
        ["LRUCache"] + ["put"]*100 + ["get"]*2,
        [[100]] + [[i, i] for i in range(100)] + [[0], [99]],
        [None] + [None]*100 + [0, 99]
    ),

    # Overflowing massive capacity
    (
        ["LRUCache"] + ["put"]*101 + ["get"]*2,
        [[100]] + [[i, i] for i in range(101)] + [[0], [100]],
        [None] + [None]*101 + [-1, 100]
    ),

    # Get operations preventing eviction
    (
        ["LRUCache", "put", "put", "put", "get", "put", "get", "get"],
        [[3], [1, 1], [2, 2], [3, 3], [1], [4, 4], [2], [1]],
        [None, None, None, None, 1, None, -1, 1]
    )
])
def test_lru_cache(commands, args, expected):
    """
    Tests the LRUCache class operations sequentially.
    Initializes the cache on the first command and validates outputs.
    """
    obj = None
    results = []
    
    for cmd, arg in zip(commands, args):
        if cmd == "LRUCache":
            obj = LRUCache(arg[0])
            results.append(None)
        elif obj is not None:
            if cmd == "put":
                obj.put(arg[0], arg[1])
                results.append(None)
            elif cmd == "get":
                results.append(obj.get(arg[0]))
                
    assert results == expected