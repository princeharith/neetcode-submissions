class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        nums.sort()

        visit = [False] * len(nums)


        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if visit[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not visit[i-1]:
                    continue

                perm.append(nums[i])
                visit[i] = True
                dfs()

                perm.pop() 
                visit[i] = False

            return
        
        dfs()
        return res
            
