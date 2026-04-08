class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        arith = set(['+', '*', '-', '/'])

        def add(num1, num2):
            return num1 + num2
        
        def sub(num1, num2):
            return num1-num2
        
        def mult(num1, num2):
            return num1 * num2
        
        def div(num1, num2):
            return int(num1/num2)

        for token in tokens:
            print(stack)
            if token not in arith:
                stack.append(int(token))
            else:
                n2, n1 = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(add(n1, n2))
                elif token == '-':
                    stack.append(sub(n1, n2))
                elif token == '*':
                    stack.append(mult(n1, n2))
                elif token == '/':
                    stack.append(div(n1, n2))
        
        return stack[-1]
                

        