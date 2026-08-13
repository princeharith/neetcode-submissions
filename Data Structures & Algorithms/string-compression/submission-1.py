class Solution:
    def compress(self, chars: List[str]) -> int:  
        s = ""
        i, k = 0, 0
        while i < len(chars):
            chars[k] = chars[i]
            j = i + 1
            k += 1
            while j < len(chars) and chars[i] == chars[j]:
                j += 1
            if (j-i) > 1:
                for digit in str(j-i):
                    chars[k] = digit
                    k += 1
            i = j
        return k
        
  
        
      
        

        



        