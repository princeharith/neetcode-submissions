class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for char in s:
            if char in close_to_open_map:
                #make sure stack exists and top of stack is the corresponding open
                if not stack or stack[-1] != close_to_open_map[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        
        return not stack


        #stack = ['('[']


        