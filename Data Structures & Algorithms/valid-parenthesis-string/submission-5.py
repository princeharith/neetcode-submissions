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
        print(open_paren)
        print(asterisk)

        if not open_paren:
            return True
        elif open_paren and not asterisk:
            return False
        else:
            while open_paren:
                if not asterisk:
                    return False
                elif open_paren.pop() > asterisk.pop():
                    return False
            return True

                    