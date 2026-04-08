class PrefixTree:

    def __init__(self):
        #dict of dicts?
        self.trie = {}

        #insert DOG

        # {
        #     d: {
        #         o: {
        #             g: {


        #             }
        #         }

        #     }
        # }
        

    def insert(self, word: str) -> None:
        curr_trie = self.trie
        for char in word:
            if char not in curr_trie:
                curr_trie[char] = {}
            #how to get trie[char]
            curr_trie = curr_trie[char]
        curr_trie['end'] = {}
        


    def search(self, word: str) -> bool:
        curr_trie = self.trie
        for char in word:
            if char not in curr_trie:
                return False
            curr_trie = curr_trie[char]
        return 'end' in curr_trie
        

    def startsWith(self, prefix: str) -> bool:
        curr_trie = self.trie
        for char in prefix:
            if char not in curr_trie:
                return False
            curr_trie = curr_trie[char]
        return True

        
        