class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(idx, curr, currSum):
            if idx == len(nums) or currSum > target:
                return
            if currSum == target:
                #why a copy?
                res.append(curr.copy())
                return
            
            curr.append(nums[idx])
            print(curr)
            print(idx)
            backtrack(idx, curr, currSum + nums[idx])
            
            curr.pop()
            backtrack(idx+1, curr, currSum)
        
        backtrack(0,[],0)
        return res

            
