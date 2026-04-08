class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)

        def isDivisor(l):
            #l is a candidate substring

            #first we check - can this candidate build the string?
                #e.g. if the candidate is ABA but one of the strings is ABAB, 
                #that cannot be repeated to create
            if l1 % l or l2 % l:
                return False
            
            f1, f2 = l1 // l, l2 // l
            #we multiply the candidate by the factor to see if we can actually make the string
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        for i in range(min(l1, l2), 0, -1):
            if isDivisor(i):
                return str1[:i]
        return ""