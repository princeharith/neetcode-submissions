class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #[F, F, F]
        #as we pick an element, change the "picked" array so that we use a different number
        res = []
        def dfs(curr, picked):
            if len(curr) == len(nums):
                res.append(curr.copy())
            for i in range(len(nums)):
                if not picked[i]:
                    curr.append(nums[i])
                    picked[i] = True
                    dfs(curr, picked)
                    
                    curr.pop()
                    picked[i] = False

        dfs([], [False]*len(nums))
        return res
                
                

        