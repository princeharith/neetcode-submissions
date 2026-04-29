class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s = "zxyzxyz"
                #  l r
        l = 0
        char_set = set()

        #char_set = set(y,z,x)
        #longest_substring = 2
        longest_substring = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            longest_substring = max(longest_substring,r-l+1)
        
        return longest_substring

        #Time: O(n)
        #Space: O(n)





        