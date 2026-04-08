class MinStack:

    def __init__(self):
        self.stack = []
        self.min_element = 2**31
        

    def push(self, val: int) -> None:
        if val < self.min_element:
            self.min_element = val
        self.stack.append(tuple([val, self.min_element]))
        

    def pop(self) -> None:
        if self.min_element == self.stack[-1][0] :
            if len(self.stack) > 1:
                self.min_element = self.stack[-2][1]
            else:
                self.min_element = 2**31
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
