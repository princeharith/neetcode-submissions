class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        

    def push(self, val: int) -> None:
        if val < self.min:
            self.stack.append((val, val))
            self.min = val
        else:
            self.stack.append((val, self.min))
        

    def pop(self) -> None:
        self.stack.pop()
        self.min = self.stack[-1][1] if self.stack else float('inf')
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
