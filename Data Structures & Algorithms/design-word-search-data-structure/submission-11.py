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
        def dfs(curr_trie, j):
            for i in range(j, len(word)):
                char = word[i]
                if char == '.':
                    for key in curr_trie:
                        if dfs(curr_trie[key], i+1):
                            return True
                    return False
                else:
                    if char not in curr_trie:
                        return False
                curr_trie = curr_trie[char]
            return 'end' in curr_trie
        
        return dfs(self.trie, 0)


        # search: b.d
        # i = 1
        # char = .


        # {
        #     b:{
        #         c:{
        #             e: {

        #             }
        #         }
        #         a: {
        #             d: {

        #             }
        #         }

        #     }
        # }

       


        
