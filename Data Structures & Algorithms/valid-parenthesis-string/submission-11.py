class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        stars = []

        #if we encounter a right ')' with no open, immediately invalid
        for i, char in enumerate(s):
            if char == '(':
                left.append(i)
            elif char == '*':
                stars.append(i)
            else:
                #we've encuntered a ')'
                if not left and not stars:
                    return False
                if left:
                    left.pop()
                elif stars:
                    stars.pop()
        
        while left and stars:
            if left.pop() > stars.pop():
                return False
        
        return not left

        