class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #nums = [-1,0,1,2,-1,-4]

        #nums = [-4,-1,-1,0,0,1,2]
                    #  i
                    #           j
                    #           k
        
        #curr_sum=1

        #res = [[-1,-1,2], [-1,0,1]]

        nums.sort()
        res = []
        #need another check for i?
        # for i in range(len(nums)-2):
        i = 0
        while i < len(nums)-2:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            j,k = i+1, len(nums)-1
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif curr_sum < 0:
                    j += 1
                else:
                    k -= 1
            i += 1
        
        return res

            
                                   