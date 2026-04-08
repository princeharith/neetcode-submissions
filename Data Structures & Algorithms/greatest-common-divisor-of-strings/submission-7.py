class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        def isGCD(i):
            if len1 % i or len2 % i:
                return False
            factor1, factor2 = len1 // i, len2 // i
            return (str1[:i] * factor1) == str1 and (str1[:i] * factor2) == str2

        for i in range(min(len1, len2), 0, -1):
            if isGCD(i):
                return str1[:i]
        return ""
