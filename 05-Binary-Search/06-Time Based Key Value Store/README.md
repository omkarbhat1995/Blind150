# Time Based Key-Value Store

This project contains the solution and testing suite for the **Time Based Key-Value Store** problem.

## Problem Description
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

## Approach
Because the problem guarantees that all the `timestamp` values in the `set` function are strictly increasing, we can safely store the values in a list (per key) and they will naturally be sorted by time.

We use a Hash Map (`defaultdict` of lists in Python) where the dictionary keys map to a list of `(timestamp, value)` tuples.
- **`set(key, value, timestamp)`**: Since the timestamps are strictly increasing, appending to the key's list takes **O(1)** time.
- **`get(key, timestamp)`**: To find the largest `timestamp_prev <= timestamp`, we can use **Binary Search** on the list of tuples. This allows us to search the history in **O(log N)** time.

## Complexity
- **Time Complexity**: 
  - `set`: O(1)
  - `get`: O(log N) where N is the number of values stored for the key.
- **Space Complexity**: O(M) where M is the total number of sets performed, as each `set` creates a new `(timestamp, value)` pair.

## Files
- `solution.py`: The `TimeMap` class implementation.
- `test_time_map.py`: 15 unit tests covering various edge cases using Python's `unittest` framework.
- `README.md`: This documentation file.

## Running Tests
Run the following command in your terminal to execute the test cases:
`python -m unittest test_time_map.py`