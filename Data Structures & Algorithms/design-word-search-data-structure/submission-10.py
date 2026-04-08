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

        
    #loop through each possible key in the trie, and go down that
    #almost like backtracking??
    def search(self, word: str) -> bool:
        
        def recurse(j, curr_trie):
            curr = curr_trie

            for i in range(j, len(word)):
                char = word[i]
                if char == '.':
                    for key in curr:
                        if recurse(i+1, curr[key]):
                            return True
                    return False
                else:
                    if char not in curr:
                        return False
                    curr = curr[char]
            return 'end' in curr
        
        return recurse(0, self.trie)

       


        
