class MinStack:

    def __init__(self):
        self.stack = []
        self.global_min = float('inf')

    def push(self, val: int) -> None:
        self.global_min = min(self.global_min, val)
        self.stack.append((val, self.global_min))

    def pop(self) -> None:
        #update min after popping
        self.stack.pop()
        if self.stack:
            self.global_min = self.stack[-1][1]
        else:
            self.global_min = float('inf')
        
    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]
        
