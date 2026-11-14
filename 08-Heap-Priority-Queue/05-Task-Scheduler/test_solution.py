import pytest
from solution import Solution

sol = Solution()

@pytest.mark.parametrize("tasks, n, expected", [
    # --- Standard LeetCode Examples ---
    (["X", "X", "Y", "Y"], 2, 5),                                       # Example 1
    (["A", "A", "A", "B", "C"], 3, 9),                                  # Example 2
    (["A", "A", "A", "B", "B", "B"], 2, 8),                             # Standard multi-max frequency

    # --- Zero Cooldown (n = 0) ---
    (["A", "A", "A", "B", "B", "B"], 0, 6),                             # No cooldown required
    (["A", "B", "C", "D", "E"], 0, 5),                                  # All unique, zero cooldown

    # --- High Cooldown ---
    (["A", "A", "A"], 100, 203),                                        # Massive cooldown, single task
    (["A", "A"], 100, 102),                                             # Massive cooldown boundary

    # --- Plenty of Fillers (Length > Baseline) ---
    (["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2, 16), # Idle slots completely filled
    (["A", "B", "C", "D", "E", "F"], 2, 6),                             # No repeats, exact length
    (["A", "B", "C", "D", "A", "B", "V"], 3, 7),                        # Fillers bridge the cooldown gap perfectly

    # --- Boundary Constraints ---
    (["A"], 0, 1),                                                      # Single task minimum bounds
    (["Z"], 100, 1),                                                    # Single task, max cooldown constraint

    # --- Multiple Identical Max Frequencies ---
    (["A", "A", "A", "B", "B", "B", "C", "C", "C"], 1, 9),              # Fits perfectly without idle time
    (["A", "B", "A", "B", "A", "B"], 3, 10),                            # A -> B -> idle -> idle -> A ...

    # --- Alphabet Saturation ---
    (["A","B","C","A","B","C"], 2, 6)                                   # Cycles perfectly into itself
])
def test_leastInterval(tasks, n, expected):
    """
    Tests the leastInterval method against 15 standard, boundary, and edge cases.
    """
    assert sol.leastInterval(tasks, n) == expected