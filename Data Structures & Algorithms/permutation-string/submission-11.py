class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        if len(s1) < len(s2):
            shorter_string = s1
            longer_string = s2
        else:
            shorter_string = s2
            longer_string = s1

        p1, p2 = 0, len(shorter_string)-1
        
        target_lst = [0]*26

        for char in shorter_string:
            target_lst[ord(char) - ord('a')] += 1
        
        #start with len up to s1
        curr_lst = [0]*26
        for i in range(len(shorter_string)):
            # print(i)
            # print(ord(s2[i]))
            # print(ord('a'))
            # print(ord(s2[i]) - ord('a'))
            curr_lst[ord(longer_string[i]) - ord('a')] += 1
        
        if curr_lst == target_lst:
            return True


        while p2 < len(longer_string)-1:
            print(curr_lst)
            p2 += 1
            curr_lst[ord(longer_string[p2]) - ord('a')] += 1
            
            curr_lst[ord(longer_string[p1]) - ord('a')] -= 1
            p1 += 1
            if curr_lst == target_lst:
                return True
        
        return False




        