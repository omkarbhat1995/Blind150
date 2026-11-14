from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Calculates the minimum number of CPU cycles required to complete all tasks.
        Uses a mathematical approach to find the baseline minimum based on the most frequent task.
        """
        task_counts = Counter(tasks)
        max_freq = max(task_counts.values())
        max_count = sum(1 for count in task_counts.values() if count == max_freq)
        
        # (max_freq - 1) gives the number of intervals where cooldown is required
        # (n + 1) is the length of each interval (1 for the task + n for the cooldown)
        # max_count is added at the end for the final execution of the most frequent tasks
        baseline_cycles = (max_freq - 1) * (n + 1) + max_count
        
        # The result is either the calculated baseline or the length of the tasks array itself
        # (if there are enough unique tasks to completely fill the idle times)
        return max(len(tasks), baseline_cycles)