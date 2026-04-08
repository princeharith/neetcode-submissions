class WordDictionary:

    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        current = self.trie

        for letter in word:
            current = current.setdefault(letter, {})
        current['_end'] = {}
        return
        

        

    def search(self, word: str) -> bool:
        print(self.trie)
        def dfs(trie, j):
            current = trie
            for i in range(j, len(word)):
                print(word[i])
                if word[i] == '.':
                    for val in current.values():
                        if dfs(val, i+1):
                            return True
                    return False
                else:
                    if word[i] not in current:
                        return False
                    current = current[word[i]]
            if '_end' in current:
                return True
            else:
                return False
        
        return dfs(self.trie, 0)

