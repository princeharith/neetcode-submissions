class Solution:

    def encode(self, strs: List[str]) -> str:
        res_str = ''
        for string in strs:
            res_str += str(len(string))
            res_str += '#'
            res_str += string
        return res_str
            

    def decode(self, s: str) -> List[str]:     
        i, j = 0,0
        res = []
        while i < len(s):
            while s[j] != '#':
                j += 1
            str_len = int(s[i:j])
            
            decoded_string = ''
            for k in range(j+1, j+str_len+1):
                decoded_string += s[k]
            res.append(decoded_string)
            j += str_len+1
            i = j

        return res


