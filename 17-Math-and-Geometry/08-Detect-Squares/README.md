# Detect Squares

**Difficulty:** Medium
**Category:** Math & Geometry / Object-Oriented Design

## Problem Description
You are given a stream of points consisting of x-y coordinates on a 2-D plane. Points can be added and queried as follows:
* **Add:** New points can be added to the stream into a data structure. Duplicate points are allowed and should be treated as separate points.
* **Query:** Given a single query point, count the number of ways to choose three additional points from the data structure such that the four points form a square with sides parallel to the x-axis and y-axis.

## Approach
To count valid squares efficiently without brute-forcing every combination of three points:
1. We maintain a Hash Map (or dictionary) that stores the frequency of every point added.
2. We maintain a list of all points added so far.
3. When querying a point `(qx, qy)`, we iterate through our list of points and treat each point `(px, py)` as the **diagonal** corner to our query point.
4. A point forms a valid diagonal if the horizontal distance equals the vertical distance `abs(qx - px) == abs(qy - py)` and the points are not identical.
5. If a valid diagonal is found, the remaining two corners of the square *must* be `(px, qy)` and `(qx, py)`.
6. We calculate the total combinations for this specific diagonal by multiplying the frequencies of the diagonal and the two required corners. 

## Complexity
* **Time Complexity:** * `add()`: $O(1)$
  * `count()`: $O(n)$, where $n$ is the number of points added so far.
* **Space Complexity:** $O(n)$ to store the points and their frequencies in the Hash Map.