class RandomizedSet:

    def __init__(self):
        self.list = []
        self.hmap = {}

    def insert(self, val: int) -> bool:
        if val not in self.hmap:
            self.hmap[val] = len(self.list)
            self.list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.hmap:
            i = self.hmap[val]
            self.list[i], self.hmap[self.list[-1]] = self.list[-1], i            
            del self.hmap[val]
            self.list.pop()
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()