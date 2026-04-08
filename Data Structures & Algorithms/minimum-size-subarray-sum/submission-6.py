class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l,r = 0,0
        curr_sum = 0
        min_size = float('inf')

        while r < len(nums):
            curr_sum += nums[r]
            if curr_sum < target:
                r += 1
                continue
            
            while curr_sum >= target and l < len(nums):
                print(curr_sum)
                print(l,r)
                min_size = min(min_size, r-l+1)
                curr_sum -= nums[l]
                l += 1
                


            r += 1
        
        return min_size if min_size != float('inf') else 0

  
        # 2,3,1,2,4,3
        #         l
        #           r

        # curr = 
        # min_size = 4 

        