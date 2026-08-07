import pytest
from solution import Solution

@pytest.mark.parametrize("points, k, expected", [
    # --- Standard LeetCode Examples ---
    ([[0, 2], [2, 2]], 1, [[0, 2]]),
    ([[0, 2], [2, 0], [2, 2]], 2, [[0, 2], [2, 0]]),
    
    # --- Edge Cases & Boundaries ---
    # 1. k equals the total number of points (Return all)
    ([[1, 3], [-2, 2]], 2, [[1, 3], [-2, 2]]),
    
    # 2. Origin point is included
    ([[0, 0], [1, 1], [2, 2]], 1, [[0, 0]]),
    
    # 3. All points are the exact same distance from origin (Points on a circle)
    ([[0, 5], [5, 0], [0, -5], [-5, 0]], 2, [[0, 5], [5, 0]]), # Expected can be any 2, test case specifically tailored
    
    # 4. Duplicate points in the array
    ([[1, 1], [1, 1], [2, 2]], 2, [[1, 1], [1, 1]]),
    
    # 5. Points strictly on the axes
    ([[0, 10], [10, 0], [0, 1], [1, 0]], 2, [[0, 1], [1, 0]]),
    
    # --- Negative Coordinates & Quadrants ---
    # 6. Completely negative coordinates
    ([[-1, -1], [-2, -2], [-3, -3]], 1, [[-1, -1]]),
    
    # 7. Points spread across all 4 quadrants
    ([[1, 1], [-1, 2], [-3, -1], [2, -2]], 2, [[1, 1], [-1, 2]]),
    
    # --- Layouts & Ordering ---
    # 8. Array already sorted by closest
    ([[1, 1], [2, 2], [3, 3]], 1, [[1, 1]]),
    
    # 9. Array sorted by farthest (Strict reverse order)
    ([[3, 3], [2, 2], [1, 1]], 1, [[1, 1]]),
    
    # 10. Alternating close and far points
    ([[1, 1], [10, 10], [2, 2], [9, 9], [3, 3]], 3, [[1, 1], [2, 2], [3, 3]]),
    
    # --- Extreme Constraints (-100 to 100) ---
    # 11. Testing maximum boundaries
    ([[100, 100], [-100, -100], [99, 99]], 1, [[99, 99]]),
    
    # 12. Testing absolute minimum boundaries with k=1
    ([[-100, 100], [100, -100], [0, 1]], 1, [[0, 1]]),
    
    # 13. Single axis extreme distances
    ([[100, 0], [0, 100], [0, 99], [99, 0]], 2, [[0, 99], [99, 0]]),
    
    # 14. Tied Distances with different axis weights (e.g. 3,4 and 4,3 and 0,5) -> all distance 5
    ([[3, 4], [5, 0], [0, 5], [4, 3], [10, 10]], 4, [[3, 4], [5, 0], [0, 5], [4, 3]]),
    
    # 15. Massive List, small k (Performance boundary simulation)
    ([[i, i] for i in range(100, 0, -1)], 3, [[1, 1], [2, 2], [3, 3]])
])
def test_kClosest(points, k, expected):
    """
    Validates kClosest against 15 unique scenarios.
    Because valid results can be returned in any order, we sort both the output 
    and the expected arrays before asserting equality to prevent false negatives.
    """
    sol = Solution()
    result = sol.kClosest(points, k)
    
    # Sort the sub-lists and then the main list to ensure order-agnostic equality
    sorted_result = sorted([sorted(p) for p in result])
    sorted_expected = sorted([sorted(p) for p in expected])
    
    # We slice expected just in case the test generator provided more equidistant 
    # points than k (like in test case 3) to safely evaluate exact match lengths.
    assert sorted_result == sorted_expected[:k]