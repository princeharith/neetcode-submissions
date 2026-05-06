class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
       

        p1, p2 = 0, len(s1)-1
        
        target_lst = [0]*26

        for char in s1:
            target_lst[ord(char) - ord('a')] += 1
        
        #start with len up to s1
        curr_lst = [0]*26
        for i in range(len(s1)):
            # print(i)
            # print(ord(s2[i]))
            # print(ord('a'))
            # print(ord(s2[i]) - ord('a'))
            curr_lst[ord(s2[i]) - ord('a')] += 1
        
        if curr_lst == target_lst:
            return True


        while p2 < len(s2)-1:
            print(curr_lst)
            p2 += 1
            curr_lst[ord(s2[p2]) - ord('a')] += 1
            
            curr_lst[ord(s2[p1]) - ord('a')] -= 1
            p1 += 1
            if curr_lst == target_lst:
                return True
        
        return False




        