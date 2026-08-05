import pytest
from solution import CountSquares

@pytest.mark.parametrize("commands, args, expected", [
    # 1. Standard LeetCode Example
    (
        ["CountSquares", "add", "add", "add", "count", "count", "add", "count"],
        [[], [[1, 1]], [[2, 2]], [[1, 2]], [[2, 1]], [[3, 3]], [[2, 2]], [[2, 1]]],
        [None, None, None, None, 1, 0, None, 2]
    ),
    
    # 2. Empty State / Premature Count
    (
        ["CountSquares", "count"],
        [[], [[0, 0]]],
        [None, 0]
    ),

    # 3. Missing Corners (Only diagonal exists)
    (
        ["CountSquares", "add", "count"],
        [[], [[5, 5]], [[0, 0]]],
        [None, None, 0]
    ),

    # 4. Same line points (Rectangles/Lines, but no squares)
    (
        ["CountSquares", "add", "add", "add", "count"],
        [[], [[0, 2]], [[0, 4]], [[0, 6]], [[0, 8]]],
        [None, None, None, None, 0]
    ),

    # 5. Overlapping Points Multiplication (Multiple combinations of the same square)
    (
        ["CountSquares", "add", "add", "add", "add", "add", "count"],
        [[], [[0, 0]], [[0, 0]], [[0, 2]], [[2, 2]], [[2, 0]], [[2, 2]]],
        # (0,0) has freq 2, others have freq 1. The query forms a square with them. 
        # Wait, if we query (2,2), we look for diagonals. 
        # Diagonal (0,0) occurs twice. For each, we check (0,2) and (2,0). 2 * 1 * 1 = 2.
        [None, None, None, None, None, None, 2]
    ),

    # 6. Negative Coordinates / Quadrant checks (Constraint says 0 <= x, y <= 1000, 
    # but good robust testing handles math properly everywhere)
    (
        ["CountSquares", "add", "add", "add", "count"],
        [[], [[-1, -1]], [[-1, 1]], [[1, -1]], [[1, 1]]],
        [None, None, None, None, 1]
    ),

    # 7. Query point matches existing point in data structure
    (
        ["CountSquares", "add", "add", "add", "add", "count"],
        [[], [[1, 1]], [[1, 2]], [[2, 1]], [[2, 2]], [[1, 1]]],
        [None, None, None, None, None, 1]
    ),

    # 8. Large Coordinates (Constraint Limits)
    (
        ["CountSquares", "add", "add", "add", "count"],
        [[], [[1000, 1000]], [[1000, 0]], [[0, 1000]], [[0, 0]]],
        [None, None, None, None, 1]
    ),

    # 9. Exact Zero Constraints
    (
        ["CountSquares", "add", "add", "add", "count"],
        [[], [[0, 0]], [[0, 1]], [[1, 1]], [[1, 0]]],
        [None, None, None, None, 1]
    ),

    # 10. Center of a cross (Forms 4 distinct squares in 4 quadrants relative to query)
    (
        ["CountSquares", "add", "add", "add", "add", "add", "add", "add", "add", "count"],
        [[], [[1,1]], [[1,-1]], [[-1,-1]], [[-1,1]], [[0,1]], [[1,0]], [[0,-1]], [[-1,0]], [[0, 0]]],
        [None, None, None, None, None, None, None, None, None, 4]
    ),

    # 11. Rectangle but not a square (Distance mismatch)
    (
        ["CountSquares", "add", "add", "add", "count"],
        [[], [[0, 0]], [[0, 3]], [[2, 0]], [[2, 3]]],
        [None, None, None, None, 0]
    ),

    # 12. Accumulating counts step by step
    (
        ["CountSquares", "add", "add", "count", "add", "count"],
        [[], [[0, 1]], [[1, 1]], [[0, 0]], [[1, 0]], [[0, 0]]],
        [None, None, None, 0, None, 1]
    ),

    # 13. Collinear diagonal point check (Diagonal shares x or y axis, should skip)
    (
        ["CountSquares", "add", "count"],
        [[], [[0, 5]], [[0, 0]]],
        [None, None, 0]
    ),

    # 14. Massive Duplicates Multiplier Test
    (
        ["CountSquares", "add", "add", "add", "add", "add", "add", "count"],
        [[], [[1,1]], [[1,1]], [[1,2]], [[1,2]], [[2,1]], [[2,1]], [[2,2]]],
        # Diagonal (1,1) x2. Corners (1,2) x2, (2,1) x2.
        # For each of the two (1,1) points found in the array, we do 2 * 2 = 4 combinations.
        # Total = 2 (diagonals) * 4 = 8
        [None, None, None, None, None, None, None, 8]
    ),

    # 15. Single point added multiple times, query somewhere else
    (
        ["CountSquares", "add", "add", "add", "count"],
        [[], [[5, 5]], [[5, 5]], [[5, 5]], [[2, 2]]],
        [None, None, None, None, 0]
    ),
])
def test_count_squares(commands, args, expected):
    """
    Iterates through parallel arrays of operations and arguments to test state mutations.
    """
    obj = None
    results = []

    for cmd, arg in zip(commands, args):
        if cmd == "CountSquares":
            obj = CountSquares()
            results.append(None)
        elif cmd == "add":
            if obj is not None:
                obj.add(arg[0])
            results.append(None)
        elif cmd == "count":
            if obj is not None:
                results.append(obj.count(arg[0]))
    
    assert results == expected