import pytest
from solution import MedianFinder

@pytest.mark.parametrize("commands, args, expected", [
    # --- Standard LeetCode Example ---
    (
        ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"],
        [[], [1], [], [3], [], [2], []],
        [None, None, 1.0, None, 2.0, None, 2.0]
    ),
    
    # --- Sequence Patterns ---
    (   # Strictly Ascending
        ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"],
        [[], [1], [], [2], [], [3], []],
        [None, None, 1.0, None, 1.5, None, 2.0]
    ),
    (   # Strictly Descending
        ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"],
        [[], [5], [], [4], [], [3], []],
        [None, None, 5.0, None, 4.5, None, 4.0]
    ),
    (   # Alternating High-Low
        ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "addNum", "findMedian"],
        [[], [10], [0], [], [9], [1], []],
        [None, None, None, 5.0, None, None, 5.0]
    ),
    (   # All Identical Numbers
        ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"],
        [[], [7], [], [7], [], [7], []],
        [None, None, 7.0, None, 7.0, None, 7.0]
    ),
    
    # --- Negative Numbers & Zero ---
    (   # Only Negatives
        ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"],
        [[], [-1], [], [-2], [], [-3], []],
        [None, None, -1.0, None, -1.5, None, -2.0]
    ),
    (   # Crossing Zero (Positives and Negatives)
        ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
        [[], [-5], [5], [], [0], []],
        [None, None, None, 0.0, None, 0.0]
    ),
    
    # --- Length Boundaries ---
    (   # Single Element
        ["MedianFinder", "addNum", "findMedian"],
        [[], [42], []],
        [None, None, 42.0]
    ),
    (   # Exactly Two Elements
        ["MedianFinder", "addNum", "addNum", "findMedian"],
        [[], [10], [20], []],
        [None, None, None, 15.0]
    ),
    (   # Exactly Three Elements
        ["MedianFinder", "addNum", "addNum", "addNum", "findMedian"],
        [[], [10], [20], [30], []],
        [None, None, None, None, 20.0]
    ),
    
    # --- Value Constraints Boundaries ---
    (   # Minimum and Maximum Constraint Values
        ["MedianFinder", "addNum", "addNum", "findMedian"],
        [[], [-100000], [100000], []],
        [None, None, None, 0.0]
    ),
    
    # --- Duplicates & Skewed Distributions ---
    (   # Heavily Skewed Left (Many Duplicates of small numbers)
        ["MedianFinder", "addNum", "addNum", "addNum", "addNum", "findMedian"],
        [[], [1], [1], [1], [100], []],
        [None, None, None, None, None, 1.0]
    ),
    (   # Heavily Skewed Right
        ["MedianFinder", "addNum", "addNum", "addNum", "addNum", "findMedian"],
        [[], [100], [100], [100], [1], []],
        [None, None, None, None, None, 100.0]
    ),
    
    # --- Continuous Interleaved Queries ---
    (   # Multiple Queries Mixed with Inserts
        ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"],
        [[], [6], [], [10], [], [2], [], [6], []],
        [None, None, 6.0, None, 8.0, None, 6.0, None, 6.0]
    ),
    
    # --- Large Value Span ---
    (   # Exponentially growing values
        ["MedianFinder", "addNum", "addNum", "addNum", "addNum", "addNum", "findMedian"],
        [[], [2], [4], [8], [16], [32], []],
        [None, None, None, None, None, None, 8.0]
    )
])
def test_median_finder(commands, args, expected):
    """
    Tests the MedianFinder logic using a sequence of commands and arguments.
    Because this is a class-design problem, we evaluate it similarly to how LeetCode does—by iterating over parallel arrays of commands and arguments[cite: 3].
    """
    obj = None
    results = []
    
    for cmd, arg in zip(commands, args):
        if cmd == "MedianFinder":
            obj = MedianFinder()
            results.append(None)
        # By nesting the operational commands under elif obj is not None:, you guarantee to the IDE that methods will only ever be called if obj has successfully been instantiated[cite: 4].
        elif cmd == "addNum" and obj is not None:
            obj.addNum(arg[0])
            results.append(None)
        elif cmd == "findMedian" and obj is not None:
            results.append(obj.findMedian())
            
    assert results == expected