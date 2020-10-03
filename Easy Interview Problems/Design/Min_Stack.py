class MinStack:

    def __init__(self):
        self.s = []
        self.minVal = float('inf') 
        

    def push(self, x: int) -> None:
        self.s.append(x)
        if x < self.minVal:
            self.minVal = x
            
    def updateMin(self):
        newMin = float('inf')
        for item in self.s:
            if item < newMin:
                newMin = item
        self.minVal = newMin

    def pop(self) -> None:
        item = self.s.pop()
        if item == self.minVal:
            self.updateMin()
        return item

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.minVal


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
