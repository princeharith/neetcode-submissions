class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(string):
            l, r = 0, len(string)-1
            while l <= r:
                if string[l] != string[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            return True
        
        res = []
        
        def backtrack(start, path):
            #whats the base case?
            if start == len(s):
                res.append(path.copy())
                return

            for end in range(start, len(s)):
                if isPalindrome(s[start:end+1]):
                    path.append(s[start:end+1])
                    backtrack(end+1, path)
                    path.pop()
        
        backtrack(0, [])
        return res