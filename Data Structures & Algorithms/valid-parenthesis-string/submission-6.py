class Solution:
    def checkValidString(self, s: str) -> bool:
        open_paren = []
        asterisk = []

        for i, char in enumerate(s):
            if char == '(':
                open_paren.append(i)
            elif char == '*':
                asterisk.append(i)
            else:
                if open_paren:
                    open_paren.pop()
                elif asterisk:
                    asterisk.pop()
                else:
                    return False

        while open_paren and asterisk:
            if open_paren.pop() > asterisk.pop():
                return False
        
        return not open_paren

                    