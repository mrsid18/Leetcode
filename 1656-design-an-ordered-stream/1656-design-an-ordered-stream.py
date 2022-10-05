class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 0
        self.list = [None]*n

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1
        self.list[idKey] = value
        res = []
        
        while self.ptr<len(self.list) and self.list[self.ptr]:
            res.append(self.list[self.ptr])
            self.ptr+=1
            
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)