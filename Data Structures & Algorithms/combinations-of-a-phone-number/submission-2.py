class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        if digits == "":
            return []

        def backtrack(idx, path):
            if len(path) == len(digits):
                res.append(''.join(path.copy()))
                return
            
            if idx == len(digits):
                return
            
            for letter in digitToChar[digits[idx]]:
                path.append(letter)
                backtrack(idx+1, path)
                path.pop()
        
        backtrack(0, [])
        return res
        