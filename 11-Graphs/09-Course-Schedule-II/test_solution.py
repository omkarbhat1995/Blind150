import pytest
from typing import List
from solution import Solution

sol = Solution()


def is_valid_order(numCourses: int, prerequisites: List[List[int]], order: List[int]) -> bool:
    """
    Verifies that `order` contains every course from 0 to numCourses - 1 exactly once
    and satisfies every [course, prereq] dependency.
    """
    if len(order) != numCourses or set(order) != set(range(numCourses)):
        return False

    position = {course: idx for idx, course in enumerate(order)}
    for course, prereq in prerequisites:
        if position[prereq] > position[course]:
            return False

    return True


@pytest.mark.parametrize("numCourses, prerequisites, is_possible", [
    # --- Standard Examples ---
    (3, [[1, 0]], True),                                                # Example 1: Simple dependency with free course
    (3, [[0, 1], [1, 2], [2, 0]], False),                               # Example 2: 3-node cycle
    (4, [[1, 0], [2, 0], [3, 1], [3, 2]], True),                        # Classic LeetCode diamond DAG

    # --- Boundaries & Minimal Cases ---
    (1, [], True),                                                      # Single course, no prerequisites
    (5, [], True),                                                      # Multiple courses, no prerequisites
    (1, [[0, 0]], False),                                               # Self-loop on a single course
    (3, [[1, 1]], False),                                               # Self-loop within a larger set

    # --- Linear Chains & Star Graphs ---
    (4, [[1, 0], [2, 1], [3, 2]], True),                                # Strict linear chain (0 -> 1 -> 2 -> 3)
    (4, [[1, 0], [2, 1], [3, 2], [0, 3]], False),                       # Full 4-node cycle
    (4, [[0, 1], [0, 2], [0, 3]], True),                                # Star graph: multiple prerequisites for one course
    (4, [[1, 0], [2, 0], [3, 0]], True),                                # Reverse star: one prerequisite unlocks many courses

    # --- Disconnected Components ---
    (4, [[1, 0], [3, 2]], True),                                        # Two separate valid chains
    (4, [[1, 0], [2, 3], [3, 2]], False),                               # One valid chain, one disconnected 2-node cycle
    (5, [[1, 0], [2, 1], [4, 3]], True),                                # Uneven disconnected valid chains

    # --- Complex Dependencies & Sub-Cycles ---
    (5, [[1, 0], [2, 1], [3, 2], [1, 3], [4, 0]], False),               # Hidden cycle (1 -> 2 -> 3 -> 1) with valid entry branch
    (5, [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]], True),                # Multi-layered valid DAG
])
def test_findOrder(numCourses, prerequisites, is_possible):
    """
    Tests the findOrder method against 16 distinct standard, boundary, and graph edge cases.
    """
    result = sol.findOrder(numCourses, prerequisites)
    if not is_possible:
        assert result == []
    else:
        assert is_valid_order(numCourses, prerequisites, result)