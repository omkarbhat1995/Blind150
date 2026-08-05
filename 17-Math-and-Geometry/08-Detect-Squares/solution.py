from typing import List
from collections import defaultdict

class CountSquares:
    """
    Data structure to store 2D points and dynamically count valid axis-aligned 
    squares that can be formed using a queried point.
    """
    def __init__(self):
        # Stores the frequency of each (x, y) coordinate
        self.point_counts = defaultdict(int)
        # Stores a continuous list of all points added to iterate over for diagonals
        self.points = []

    def add(self, point: List[int]) -> None:
        """
        Adds a new point to the data structure. Duplicate points are tallied.
        """
        x, y = point
        self.point_counts[(x, y)] += 1
        self.points.append((x, y))

    def count(self, point: List[int]) -> int:
        """
        Counts the number of valid squares that can be formed using the given point
        and three previously added points.
        """
        qx, qy = point
        total_squares = 0

        # Treat every added point as a potential diagonal opposite to (qx, qy)
        for px, py in self.points:
            # Check if it forms a valid square diagonal (equal width and height)
            # and ensure it's not the exact same point as the query point
            if abs(qx - px) != abs(qy - py) or px == qx or py == qy:
                continue
            
            # If it's a valid diagonal, the other two corners must exist
            corner1 = (px, qy)
            corner2 = (qx, py)
            
            # Multiply the frequencies of the three required points
            # If any are missing, the multiplier handles the 0 automatically
            total_squares += self.point_counts[corner1] * self.point_counts[corner2]

        return total_squares