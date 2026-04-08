class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(idx, curr_sum, curr_list):
            if curr_sum > target:
                return
            elif idx == len(candidates):
                if curr_sum == target:
                    res.append(curr_list.copy())
                    return
                else:
                    return
            
            curr_list.append(candidates[idx])
            backtrack(idx+1, curr_sum+candidates[idx], curr_list)

            while idx < len(candidates)-1 and candidates[idx] == candidates[idx+1]:
                idx += 1

            curr_list.pop()
            backtrack(idx+1, curr_sum, curr_list)
        
        backtrack(0, 0, [])
        return res

