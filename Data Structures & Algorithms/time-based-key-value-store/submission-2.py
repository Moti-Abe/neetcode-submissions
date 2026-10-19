class TimeMap:

    def __init__(self):
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = [(value, timestamp)]
        else:
            self.mp[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.mp.get(key)
        if arr is None: return ""
        l, r = 0, len(arr)-1
        mid = 0
        while l <= r:
            mid = (l+r)//2
            if arr[mid][1] < timestamp:
                l = mid+1
            elif arr[mid][1] > timestamp:
                r = mid-1
            else:
                return arr[mid][0]
        if r < 0: return ""        
        return arr[r][0]