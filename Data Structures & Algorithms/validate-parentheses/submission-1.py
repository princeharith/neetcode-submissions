class Solution:
    def isValid(self, s: str) -> bool:
        closed_paren = {
        ')': '(', 
        '}': '{', 
        ']': '['
        }

        stack = []

        for char in s:
            if char in closed_paren and not stack:
                return False
            elif char in closed_paren:
                if stack[-1] == closed_paren[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)    

        return True if not stack else False           