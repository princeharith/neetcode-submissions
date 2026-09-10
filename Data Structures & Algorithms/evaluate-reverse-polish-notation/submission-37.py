class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        #add numbers to the stack
        #if we reach an operator, take the top 2 items on the stack

        """
        stack = [2, 4]
        """

        operators = set({'+', '/', '*', '-'})
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(token)
                continue

            num2, num1 = stack.pop(), stack.pop()
            num1, num2 = int(num1), int(num2)
            if token == '+':
                stack.append(num1+num2)
            elif token == '*':
                stack.append(num1*num2)
            elif token == '-':
                stack.append(num1-num2)
            elif token == '/':
                stack.append(num1/num2)
        
        return int(stack[0])

        