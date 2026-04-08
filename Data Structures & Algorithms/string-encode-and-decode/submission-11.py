class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for string in strs:
            len_string = len(string)
            res += f'{len_string}'
            res += '#'
            res += string
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i = 0
        while i < (len(s)):
            j = i
            while j < len(s) and s[j] != '#':
                j+= 1
            print(s[i:j])
            word_len = int(s[i:j])
            word = s[j+1:j+1+word_len]
            res.append(word)
            i = j + word_len + 1
        
        return res

            


