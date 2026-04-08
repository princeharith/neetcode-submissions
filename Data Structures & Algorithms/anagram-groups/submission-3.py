class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        
        for string in strs:
            letters = [0]*26
            for letter in string:
                letter_index = ord(letter) - ord('a')
                letters[letter_index] += 1
            letters = tuple(letters)
            hashmap[letters].append(string)
        
        #return [v for v in hashmap.values()]
        return list(hashmap.values())


       
                

        