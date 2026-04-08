class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = collections.Counter(s)
        count_t = collections.Counter(t)

        return count_s == count_t
