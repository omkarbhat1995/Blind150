class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculates the number of distinct ways to climb to the top of an n-step staircase,
        taking either 1 or 2 steps at a time.
        Uses space-optimized Bottom-Up Dynamic Programming (Fibonacci sequence).
        """
        if n <= 2:
            return n

        one_step_before = 2
        two_steps_before = 1

        # Ways to reach step i = ways to reach (i - 1) + ways to reach (i - 2)
        for _ in range(3, n + 1):
            current = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = current

        return one_step_before