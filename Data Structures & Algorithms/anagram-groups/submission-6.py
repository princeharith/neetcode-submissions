class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for word in strs:
            char_list = [0] * 26
            for char in word:
                char_list[ord(char) - ord('a')] += 1
            anagram_dict[tuple(char_list)].append(word)
        

        res = []
        for k,v in anagram_dict.items():
            res.append(v)
        
        return res
            