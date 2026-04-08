class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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
        res = []
        def dfs(i, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return
            
            num = digits[i]
            for letter in digitToChar[num]:
                dfs(i+1, curr+letter)
        if digits:
            dfs(0, '')
        return res
        