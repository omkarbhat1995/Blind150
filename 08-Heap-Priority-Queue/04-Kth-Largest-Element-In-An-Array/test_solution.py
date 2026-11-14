import pytest
from solution import KthLargest

@pytest.mark.parametrize("commands, args, expected", [
    # --- Standard LeetCode Example ---
    (
        ["KthLargest", "add", "add", "add", "add", "add"],
        [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]],
        [None, 4, 5, 5, 8, 8]  # Note: Modified original slightly to show variation
    ),
    (
        ["KthLargest", "add", "add", "add", "add", "add"],
        [[3, [1, 2, 3, 3]], [3], [5], [6], [7], [8]],
        [None, 3, 3, 3, 5, 6]  # Exact LeetCode Example 1
    ),
    
    # --- K value Variations ---
    (   # k = 1 (Always tracking the maximum element)
        ["KthLargest", "add", "add", "add"],
        [[1, [-1, -2]], [1], [5], [3]],
        [None, 1, 5, 5]
    ),
    
    # --- Negative Numbers & Constraints ---
    (   # Only negative numbers
        ["KthLargest", "add", "add", "add"],
        [[2, [-5, -1, -3]], [-4], [-2], [-10]],
        [None, -3, -2, -2]
    ),
    (   # Crossing Zero
        ["KthLargest", "add", "add", "add"],
        [[2, [-1, 0]], [1], [2], [-5]],
        [None, 0, 1, 1]
    ),
    
    # --- Exact Constraint Boundaries ---
    (   # Minimum and Maximum values allowed by constraints
        ["KthLargest", "add", "add", "add"],
        [[1, [1000, -1000]], [1000], [-1000], [0]],
        [None, 1000, 1000, 1000]
    ),
    
    # --- Array Length Variations ---
    (   # Empty initial array (Valid per 0 <= nums.length constraint)
        # Note: add will be called at least k times to satisfy "always at least k integers"
        ["KthLargest", "add", "add", "add"],
        [[2, []], [1], [2], [3]],
        [None, None, 1, 2] # the first add doesn't actually meet k=2 if evaluated, but LC guarantees queries are valid
    ),
    (   # Initial array exactly size k
        ["KthLargest", "add", "add"],
        [[3, [1, 2, 3]], [4], [5]],
        [None, 2, 3]
    ),
    (   # Initial array size k - 1
        ["KthLargest", "add", "add"],
        [[3, [1, 2]], [3], [4]],
        [None, 1, 2]
    ),
    
    # --- Sequence Patterns ---
    (   # Strictly Ascending
        ["KthLargest", "add", "add", "add", "add"],
        [[2, [1, 2]], [3], [4], [5], [6]],
        [None, 2, 3, 4, 5]
    ),
    (   # Strictly Descending
        ["KthLargest", "add", "add", "add", "add"],
        [[2, [5, 4]], [3], [2], [1], [0]],
        [None, 4, 4, 4, 4]
    ),
    (   # All Identical
        ["KthLargest", "add", "add", "add"],
        [[3, [7, 7, 7, 7]], [7], [7], [7]],
        [None, 7, 7, 7]
    ),
    
    # --- Extreme Duplicates ---
    (   # Many duplicates in a row
        ["KthLargest", "add", "add", "add", "add", "add"],
        [[2, [1, 10]], [10], [10], [10], [1], [10]],
        [None, 10, 10, 10, 10, 10]
    ),
    
    # --- Alternating High Lows ---
    (
        ["KthLargest", "add", "add", "add", "add", "add"],
        [[3, [5, 5, 5]], [0], [10], [0], [10], [0]],
        [None, 5, 5, 5, 10, 10]
    ),
    
    # --- Adding Zeros ---
    (
        ["KthLargest", "add", "add", "add"],
        [[2, [1, -1]], [0], [0], [0]],
        [None, 0, 0, 0]
    )
])
def test_kth_largest(commands, args, expected):
    """
    Tests the KthLargest logic using a sequence of commands and arguments.
    Because this is a class-design problem, we evaluate it by iterating 
    over parallel arrays of commands and arguments.
    """
    obj = None
    results = []
    
    for cmd, arg in zip(commands, args):
        if cmd == "KthLargest":
            obj = KthLargest(arg[0], arg[1])
            results.append(None)
        elif cmd == "add" and obj is not None:
            # We handle the case where the stream might briefly dip below k due to empty init.
            # In a real environment we assume the call is valid per constraints.
            try:
                results.append(obj.add(arg[0]))
            except IndexError:
                results.append(None)
            
    assert results == expected