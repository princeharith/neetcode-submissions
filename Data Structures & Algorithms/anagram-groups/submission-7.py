class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            dict_key = [0] * 26
            for char in string:
                dict_key[ord(char) - ord('a')] += 1
            anagrams[tuple(dict_key)].append(string)
        
        res = []
        for k, v in anagrams.items():
            res.append(v)
        
        return res

