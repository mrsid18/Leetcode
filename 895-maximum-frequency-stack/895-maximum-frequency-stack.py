class FreqStack:

    def __init__(self):
        self.stacks = {}
        self.cnt = {}
        self.maxcnt = 0

    def push(self, val: int) -> None:
        self.cnt[val] = self.cnt.get(val, 0) + 1
        
        if self.cnt[val] > self.maxcnt:
            self.maxcnt = self.cnt[val]
            self.stacks[self.maxcnt] = []
        
        self.stacks[self.cnt[val]].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxcnt]
        output = res.pop()
        self.cnt[output] -= 1 if self.cnt[output] else 0
        if not res:
            self.maxcnt -= 1 if self.maxcnt else 0
        
        return output


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()