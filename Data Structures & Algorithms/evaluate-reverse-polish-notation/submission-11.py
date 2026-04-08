class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #[1,2,+,3,4,+,*]
        #[1,2,+]
        import operator

        if len(tokens) == 1:
            return int(tokens[0])

        operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
        }


        
        #[1,2,+,3,*]
        #[3,3,*]
        stack = []
        for char in tokens:
            if char not in operators:
                stack.append(char)
            else:
                func = operators[char]
                digit2, digit1 = stack.pop(), stack.pop()
                new_num = func(int(digit1), int(digit2))
                print(new_num)
                stack.append(new_num)
        return int(stack[0])

        #stack = [10,6,9,3,+]

        #stack = [9, 4]

