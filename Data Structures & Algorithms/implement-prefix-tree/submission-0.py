class PrefixTree:

    def __init__(self):
        self.root = dict()
        

    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            current = current.setdefault(letter, {})
        current['_end'] = {}

    def search(self, word: str) -> bool:
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        if '_end' in current:
            return True
        return False
    

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for letter in prefix:
            if letter not in current:
                return False
            current = current[letter]
        return True

        
        