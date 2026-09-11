class Solution:
    def isValid(self, s: str) -> bool:


        """
        #only append opens to our stack
        #if we see a close, top of stack must be a matching open
            #if no stack, return false
            #if not match, return false
        
        #if stack not empty, return false
        """
        
        matching_paren = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for char in s:
            if char not in matching_paren:
                stack.append(char)
                continue
            else:
                if not stack or stack[-1] != matching_paren[char] :
                    return False
                stack.pop()
        
        return False if stack else True