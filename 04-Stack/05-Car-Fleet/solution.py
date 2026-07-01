from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair up the positions and speeds, then sort them by position descending
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []
        
        for p, s in sorted(pair, reverse=True):
            # Calculate the time to reach the target as a float
            print(f"Car at position {p} with speed {s} will take {(target - p) / s:.2f} seconds to reach the target.")
            time_to_target = (target - p) / s
            stack.append(time_to_target)
            
            # If the car behind reaches the target in less or equal time, it catches up
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)
    
sol = Solution()
print(sol.carFleet(10, [0, 1, 2, 3], [4, 3, 2, 1]))  # Output: 3