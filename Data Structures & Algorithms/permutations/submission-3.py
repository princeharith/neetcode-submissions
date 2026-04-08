class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def backtrack(idx, curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i in range(0, len(nums)):
                print(i)
                if not used[i]:
                    curr.append(nums[i])
                    used[i] = True
                    print(f'about to call backtrack with num {i}')
                    backtrack(i+1, curr)

                    curr.pop()
                    used[i] = False
            
        backtrack(0, [])
        return res
        