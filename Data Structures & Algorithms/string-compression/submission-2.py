class Solution:
    def compress(self, chars: List[str]) -> int:
        # ["a","a","a","a","a","b","c","c","c","c","c"]
        #                                              r
        #                           l
        #count = 5
        
        s = ""
        l,w = 0,0
        while l < len(chars):
            r = l + 1
            count = 1
            #s += chars[l]
            chars[w] = chars[l]
            w += 1

            while r < len(chars) and chars[r] == chars[l]:
                count += 1
                r += 1
            
            if (r-l) > 1:
                for num_char in str(r-l):
                    #s += num_char
                    chars[w] = num_char
                    w += 1
            l = r
        
        return w
        
        
                



