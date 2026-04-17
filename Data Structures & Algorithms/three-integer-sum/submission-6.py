class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort
        #fix 1 number
        #then make it a 2 sum (avoid duplicates)

        nums.sort() #O(nlogn)

        # [-1,0,1,2,-1,4]
        # nums=[-1,0,1,2,-1,-4]
        #[-4,-1,-1,0,1,2]
        #     i  j     k

        #[-1,0,1,2,-1,-4]
        #[-4,-1,-1,0,1,2]
            #   i  j     k

        res = []
        i = 0

        while i < len(nums):
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            j,k = i+1, len(nums)-1
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif curr_sum > 0:
                    #decrease k
                    k -= 1
                else:
                    j += 1
            i += 1
        
        return res


