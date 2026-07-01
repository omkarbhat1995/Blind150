from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # will store pairs: [temp, index]

        for i, t in enumerate(temperatures):
            # While stack is not empty and current temp is greater than the top of stack
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            
            # Push current day onto the stack
            stack.append([t, i])
            
        return res