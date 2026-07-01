from collections import defaultdict

class TimeMap:
    def __init__(self):
        # Dictionary to store key -> list of (timestamp, value)
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Since timestamps are strictly increasing, we just append
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # If the key doesn't exist at all, return empty string
        if key not in self.store:
            return ""
            
        values = self.store[key]
        
        # Binary search to find the largest timestamp_prev <= timestamp
        left, right = 0, len(values) - 1
        res = ""
        
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1
                
        return res