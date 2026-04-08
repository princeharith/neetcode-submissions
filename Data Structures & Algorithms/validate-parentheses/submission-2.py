class Solution:
    def isValid(self, s: str) -> bool:
        closed_paren = {
        ')': '(', 
        '}': '{', 
        ']': '['
        }

        stack = []

        for char in s:
            if char not in closed_paren:
                stack.append(char)
            elif stack and stack[-1] == closed_paren[char]:
                stack.pop()
            else:
                return False

        return True if not stack else False           