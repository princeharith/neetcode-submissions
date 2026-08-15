class Solution:
    def compress(self, chars: List[str]) -> int:
        # ["a","a","a","a","a","b","c","c","c","c","c"]
        #                       r
        #                       l
        #count = 5

        l,w = 0,0
        s = ""
        

        while l < len(chars):
            r = l + 1
            chars[w] = chars[l]
            w += 1
            while r < len(chars) and chars[l] == chars[r]:
                r += 1
            if (r-l) > 1:
                for digit in str(r-l):
                    chars[w] = digit
                    l += 1
                    w += 1
            
            l = r
        
        return w
        

            



        
        
                



