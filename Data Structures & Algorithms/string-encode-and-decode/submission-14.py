class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for string in strs:
            len_string = len(string)
            res+= str(len(string))
            res+='#'
            res+=string
        
        # print(res)
        return res

    def decode(self, s: str) -> List[str]:
        5#Hello5#World

        res = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
            str_len = int(s[i:j])
            word = s[j+1:j+1+str_len]
            res.append(word)
            i = j + str_len+1
        
        return res

            
        
        
