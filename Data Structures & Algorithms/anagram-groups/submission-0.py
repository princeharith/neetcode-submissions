class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        char_counts = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1

            tup_count = tuple(count)
            char_counts[tup_count].append(string)

        return char_counts.values()
        
