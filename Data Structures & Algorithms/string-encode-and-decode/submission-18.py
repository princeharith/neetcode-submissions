class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''

        for s in strs:
            res += str(len(s))
            res += '#'
            res += s
        
        return res
            


    def decode(self, s: str) -> List[str]:
        res = []
        # 3#ABC
        # i
        #  j


        i, j = 0, 0
        print(s)
        while i < len(s):
            while s[j] != '#':
                j += 1
            print(i,j)
            word_len = int(s[i:j])

            curr_string = ''
            for k in range(j+1, j+word_len+1):
                curr_string += s[k]
            res.append(curr_string)

            j += (word_len + 1)
            i = j

        return res




        
