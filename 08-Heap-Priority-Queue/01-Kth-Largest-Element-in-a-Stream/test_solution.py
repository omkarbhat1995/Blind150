import pytest
from solution import KthLargest

@pytest.mark.parametrize("commands, args, expected", [
    # --- Standard LeetCode Examples ---
    (
        ["KthLargest", "add", "add", "add", "add", "add"],
        [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]],
        [None, 4, 5, 5, 8, 8]
    ),
    
    # --- Edge Cases & Boundaries ---
    (   # Empty initial array (allowed by constraints)
        ["KthLargest", "add", "add", "add", "add", "add"],
        [[1, []], [-3], [-2], [-4], [0], [4]],
        [None, -3, -2, -2, 0, 4]
    ),
    (   # k = 1 (essentially a tracking max-val stream)
        ["KthLargest", "add", "add", "add"],
        [[1, [1, 2, 3]], [4], [0], [10]],
        [None, 4, 4, 10]
    ),
    (   # All Identical Elements
        ["KthLargest", "add", "add", "add"],
        [[2, [0, 0, 0, 0]], [0], [0], [0]],
        [None, 0, 0, 0]
    ),
    (   # Purely Negative Values
        ["KthLargest", "add", "add", "add"],
        [[3, [-1, -2, -3, -4, -5]], [-1], [-1], [-1]],
        [None, -2, -1, -1]
    ),
    
    # --- Dynamic Stream Shifts ---
    (   # Adding values strictly smaller than the kth largest (Heap doesn't change bottom)
        ["KthLargest", "add", "add", "add"],
        [[2, [10, 20, 30]], [5], [1], [-100]],
        [None, 20, 20, 20]
    ),
    (   # Adding values strictly larger than everything (Forces multiple pops)
        ["KthLargest", "add", "add", "add"],
        [[2, [1, 2, 3]], [10], [20], [30]],
        [None, 3, 10, 20]
    ),
    (   # Alternating high and low values
        ["KthLargest", "add", "add", "add", "add"],
        [[3, [1, 5, 10]], [-1], [100], [0], [200]],
        [None, 1, 5, 5, 10]
    ),
    
    # --- Exact Constraint Limits ---
    (   # Initial array length exactly equals k
        ["KthLargest", "add", "add"],
        [[4, [1, 2, 3, 4]], [5], [0]],
        [None, 2, 2]
    ),
    (   # Massive initialization, small k
        ["KthLargest", "add", "add"],
        [[2, [i for i in range(1000)]], [2000], [3000]],
        [None, 999, 2000]
    ),
    (   # Large initial array, descending order
        ["KthLargest", "add", "add"],
        [[3, [10, 9, 8, 7, 6, 5, 4]], [11], [12]],
        [None, 9, 10]
    ),
    (   # Large initial array, ascending order
        ["KthLargest", "add", "add"],
        [[3, [1, 2, 3, 4, 5, 6, 7]], [8], [9]],
        [None, 6, 7]
    ),
    
    # --- Extreme Constraint Boundaries (-1000 to 1000) ---
    (   # Testing absolute lower bounds
        ["KthLargest", "add", "add", "add"],
        [[2, [-1000, -1000, -1000]], [-1000], [0], [1000]],
        [None, -1000, -1000, 0]
    ),
    (   # Testing absolute upper bounds
        ["KthLargest", "add", "add", "add"],
        [[2, [1000, 1000, 1000]], [1000], [500], [1000]],
        [None, 1000, 1000, 1000]
    ),
    (   # Duplicate bounds
        ["KthLargest", "add", "add", "add"],
        [[1, [-1000]], [1000], [-1000], [1000]],
        [None, 1000, 1000, 1000]
    )
])
def test_kthLargest(commands, args, expected):
    """
    Validates KthLargest object behavior against 15 unique constraint variations.
    """
    obj = None
    results = []
    
    for cmd, arg in zip(commands, args):
        if cmd == "KthLargest":
            # arg[0] is k, arg[1] is the initial nums list
            obj = KthLargest(arg[0], arg[1])
            results.append(None)
        elif cmd == "add":
            # Type-safe check to appease the linter
            if obj is not None:
                results.append(obj.add(arg[0]))
                
    assert results == expected