from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Calculates the minimum cost to reach the top of the staircase (past the last index).
        Uses space-optimized Bottom-Up Dynamic Programming without modifying the input array.
        """
        # You can start at index 0 or index 1 with zero initial cost
        two_steps_before = 0
        one_step_before = 0

        # Min cost to reach floor i = min(cost to reach i - 1 + cost[i - 1],
        #                                 cost to reach i - 2 + cost[i - 2])
        for i in range(2, len(cost) + 1):
            current = min(
                one_step_before + cost[i - 1],
                two_steps_before + cost[i - 2],
            )
            two_steps_before = one_step_before
            one_step_before = current

        return one_step_before