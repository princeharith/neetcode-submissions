class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #What is the time space compelexity?
        adj_list = {}
        adj_list = defaultdict(set)
        # for w in words:
        #     for c in w:
        #         adj_list[c] = set()
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            min_length = min(len(word1), len(word2))
            if word1[:min_length] == word2[:min_length] and len(word1) > len(word2):
                return ""
            for j in range(len(word1)):
                if word1[j] != word2[j]:
                    char = word1[j]
                    adj_list[char].add(word2[j])
                    break
        
        res = []
        visited = set()
        curr_cycle = set()
        def dfs(char):
            if char in visited:
                return True
            if char in curr_cycle:
                return False
            curr_cycle.add(char)

            for nei in adj_list[char]:
                if not dfs(nei):
                    return False
            curr_cycle.remove(char)
            visited.add(char)
            res.append(char)
            return True
        
        for w in words:
            for c in w:
                if not dfs(c):
                    return ""
        return "".join(reversed(res))

        # for c in adj_list:
        #     if not dfs(c):
        #         return ""
        # return "".join(reversed(res))
            

        




        #if two string have the same prefix, and smaller comes second, then we return ""
        #cycle would mean invalid



        