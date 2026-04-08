class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #dictionary where key is [0,0,0,0,0]...
        #each index represents char from a...z
        #if a word has the same frequency of chars, we append to that key's value

        anagram_groups = defaultdict(list)

        for word in strs:
            char_count = [0]*26
            for char in word:
                char_idx = ord(char) - ord('a')
                char_count[char_idx] += 1
            anagram_groups[tuple(char_count)].append(word)
        
        res = []
        for k,v in anagram_groups.items():
            res.append(v)
        
        return res
        
        