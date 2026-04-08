class WordDictionary:

    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        curr_trie = self.trie
        for char in word:
            if char not in curr_trie:
                curr_trie[char] = {}
            curr_trie = curr_trie[char]
        curr_trie['_end'] = {}
        


    #say we want to match "a.e"
        #we need to try every key in the curr trie
    def search(self, word: str) -> bool:

        def helper(j, curr_trie):
            for i in range(j, len(word)):
                char = word[i]
                if char == '.':
                    for key in curr_trie:
                        if helper(i+1, curr_trie[key]):
                            return True
                        return False
                if char not in curr_trie:
                    return False
                curr_trie = curr_trie[char]
            if '_end' in curr_trie:
                return True
            return False
        
        return helper(0, self.trie)
        
