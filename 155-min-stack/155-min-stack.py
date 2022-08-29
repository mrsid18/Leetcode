class MinStack:
    
    def __init__(self):
        self.stack = []
        self.min = []
        
    def push(self, val):
        self.stack.append(val)
        minVal = val
        if self.min and self.min[-1]<minVal: minVal = self.min[-1]
        self.min.append(minVal)
    
    def pop(self):
        num = self.stack.pop()
        self.min.pop()
        return num
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()