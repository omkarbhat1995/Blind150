from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # Will store pairs: (index, height)

        for i, h in enumerate(heights):
            start = i
            # If current height is less than the top of the stack, pop and calculate area
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                # The current bar can extend backward to where the popped bar started
                start = index
            
            stack.append((start, h))

        # Calculate area for any remaining bars in the stack
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area