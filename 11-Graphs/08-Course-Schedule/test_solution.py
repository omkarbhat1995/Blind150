import pytest
from solution import Solution

sol = Solution()


@pytest.mark.parametrize("numCourses, prerequisites, expected", [
    # --- Standard LeetCode Examples ---
    (2, [[0, 1]], True),                                               # Example 1: Simple valid dependency
    (2, [[0, 1], [1, 0]], False),                                      # Example 2: Direct 2-node cycle

    # --- Boundaries & Minimal Cases ---
    (1, [], True),                                                     # Single course, no prerequisites
    (5, [], True),                                                     # Multiple courses, no prerequisites
    (1, [[0, 0]], False),                                              # Self-loop on a single course
    (3, [[1, 1]], False),                                              # Self-loop within a larger set

    # --- Linear Chains & DAG Structures ---
    (4, [[1, 0], [2, 1], [3, 2]], True),                               # Valid linear chain (0 -> 1 -> 2 -> 3)
    (4, [[1, 0], [2, 1], [3, 2], [0, 3]], False),                      # Full 4-node cycle
    (4, [[1, 0], [2, 0], [3, 1], [3, 2]], True),                       # Diamond DAG (converging paths, no cycle)
    (4, [[0, 1], [0, 2], [0, 3]], True),                               # Star graph: multiple prerequisites for one course
    (4, [[1, 0], [2, 0], [3, 0]], True),                               # Reverse star: one prerequisite unlocks many courses

    # --- Disconnected Components ---
    (4, [[1, 0], [3, 2]], True),                                       # Two separate valid chains
    (4, [[1, 0], [2, 3], [3, 2]], False),                              # One valid chain, one disconnected cycle
    (5, [[1, 0], [2, 1], [4, 3]], True),                               # Uneven disconnected valid chains

    # --- Complex Dependencies & Sub-Cycles ---
    (5, [[1, 0], [2, 1], [3, 2], [1, 3], [4, 0]], False),              # Hidden cycle (1 -> 2 -> 3 -> 1) with valid entry branch
    (5, [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]], True),               # Multi-layered valid DAG
])
def test_canFinish(numCourses, prerequisites, expected):
    """
    Tests the canFinish method against 16 distinct standard, boundary, and graph edge cases.
    """
    assert sol.canFinish(numCourses, prerequisites) == expected