class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #have a master res list

        #backtracking helper
            #if idx is length of nums, add a copy? of curr to res

            #otherwise, add the current num to current list
            #call backtrack with new curr, idx + 1

            #pop from curr
            #call backtrack again, with idx + 1
        
        res = []

        def backtrack(idx, curr_list):
            if idx == len(nums):
                res.append(curr_list.copy())
                return
           
            curr_list.append(nums[idx])
            backtrack(idx+1, curr_list)

            curr_list.pop()
            backtrack(idx+1, curr_list)
        backtrack(0, [])
        return res




        