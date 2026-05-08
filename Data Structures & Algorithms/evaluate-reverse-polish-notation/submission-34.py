class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ['+', '-', '*', '/']



        for token in tokens:
            print(stack)
            if token not in operands:
                stack.append(int(token))
            else:
                operand2, operand1 = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(operand1+operand2)
                elif token == '-':
                    stack.append(operand1-operand2)
                elif token == '/':
                    stack.append(int(operand1 / operand2))
                elif token == '*':
                    stack.append(operand1 * operand2)

        return stack[0]      

        # stack = [5]
        # token = '-'
        # operand1, operand2 = 9, 4
        