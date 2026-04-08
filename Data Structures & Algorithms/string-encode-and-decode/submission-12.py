class Solution:

    def encode(self, strs: List[str]) -> str:
        final_string = ""
        for string in strs:
            #When we build our encoded string, we need to do number, then 'delimiter'
            #This is because this way, when we have two pointer below, the slice 
            #of s[i:j] will correspond to the number
            length = len(string)
            final_string += str(length)
            final_string += '%'
            final_string += string
        return final_string


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i 
            while j < len(s) and s[j] != '%':
                j += 1
            str_len = int(s[i:j])
            word = s[j+1:j+1+str_len]
            res.append(word)
            i = j+str_len+1
        
        return res


    
        
        return res


                



        return
