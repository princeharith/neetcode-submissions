class Solution:
    def isValid(self, s: str) -> bool:
        closed_map = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        stack = []

        for char in s:
            if char in closed_map:
                if not stack:
                    return False
                elif stack[-1] != closed_map[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        return True if not stack else False
                
        