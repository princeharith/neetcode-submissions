class WordDictionary:

    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        curr_trie = self.trie

        for char in word:
            if char not in curr_trie:
                curr_trie[char] = {}
            curr_trie = curr_trie[char]
        curr_trie['end'] = {}
        

    def search(self, word: str) -> bool:

        def dfs(j, curr_trie):
            for i in range(j, len(word)):
                char = word[i]
                if char == '.':
                    for key in curr_trie:
                        if dfs(i+1, curr_trie[key]):
                            return True
                    return False
                if char not in curr_trie:
                    return False
                curr_trie = curr_trie[char]
            
            return 'end' in curr_trie
                
                
        return dfs(0, self.trie)

        
