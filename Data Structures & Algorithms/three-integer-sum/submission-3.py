class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        res = []
        nums.sort()
        for i in range(len(nums)):
            j,k = i+1, len(nums)-1
            
            #This is also to prevent duplicates that start with i
            #The i > 0 is to make sure we are inbounds before the actual check
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    #This prevents duplicates for j and k
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        
        return res
        