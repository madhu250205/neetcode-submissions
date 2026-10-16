class TimeMap:

    def __init__(self):
        # Dictionary mapping key -> list of [value, timestamp] pairs
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        
        # Binary search to find the largest timestamp <= target timestamp
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]  # Valid candidate, try looking for a closer/larger one on the right
                l = mid + 1
            else:
                r = mid - 1  # Too large, search left
                
        return res