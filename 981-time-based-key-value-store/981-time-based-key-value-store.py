class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.store:
            l, r = 0, len(self.store[key])-1
            
            while l<=r:
                mid=(l+r)//2
                val, time = self.store[key][mid]
                if time==timestamp:
                    return val
                elif time>timestamp:
                    r=mid-1
                else: 
                    l = mid+1
                    res = val
        
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)