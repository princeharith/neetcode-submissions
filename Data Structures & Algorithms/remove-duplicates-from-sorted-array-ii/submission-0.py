class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [0,0,1,1,1,1,2,3,3]
        #  i
        #      j
        # count: 2

        
        i, j = 0,0

        while i < len(nums):
            count = 1
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                count += 1
                i += 1
            
            for _ in range(min(2, count)):
                nums[j] = nums[i]
                j += 1
            print(j)
            print("exited loop")

            i += 1
        
        return j


            

        
        