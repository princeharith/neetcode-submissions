class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #k represents the res list, e.g. the base case
        res = []
        def backtrack(curr, idx):
            if idx == n:
                if len(curr) == k:
                    res.append(curr.copy())
                return
            curr.append(idx+1)
            backtrack(curr, idx+1)
            curr.pop()
            backtrack(curr, idx+1)
        
        backtrack([], 0)
        return res
            
            
            # [1,2,3]
            # curr = [1]
            #     curr = [1,2]
            #         curr = [1,2,3]
            # curr = [2]
        