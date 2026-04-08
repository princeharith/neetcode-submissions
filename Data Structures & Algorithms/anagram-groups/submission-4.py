class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)



        for string in strs:
            char_tup = [0] * 26
            for char in string:
                char_index = ord(char) - ord('a')
                char_tup[char_index] += 1
            anagrams[tuple(char_tup)].append(string)
        
        res = []
        for k,v in anagrams.items():
            res.append(v)
        
        return res


    
        
        