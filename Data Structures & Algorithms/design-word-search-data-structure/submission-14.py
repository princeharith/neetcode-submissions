class WordDictionary:

    def __init__(self):
        self.trie = {}

    #     {
    #         'a': 
    #         {
    #             'b': {
    #                 'end': {}
    #             }
    #         }, 
    #         {
    #             'c': 
    #             {
    #                 'd': {
    #                     'end': {}
    #                 }
    #             }
    #         }
    #     }
        
    # a.d

    def addWord(self, word: str) -> None:
        curr_trie = self.trie
        for char in word:
            if char not in curr_trie:
                curr_trie[char] = {}
            curr_trie = curr_trie[char]
        curr_trie['end'] = {}
        

    def search(self, word: str) -> bool:
        def helper(curr_trie, j):
            for i in range(j, len(word)):
                char = word[i]
                if char == '.':
                    for key in curr_trie:
                        if helper(curr_trie[key], i+1):
                            return True
                    return False
                if char not in curr_trie:
                    return False
                curr_trie = curr_trie[char]
            return 'end' in curr_trie
        
        return helper(self.trie, 0)
                    #keep track of the index


        
