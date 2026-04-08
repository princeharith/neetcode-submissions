class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bfs(nums,l, r, target):
            while l <= r:
                m = (l+r)//2
                print(l, r)
                print(m)

                if nums[m] == target:
                    return m
                
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1


        l,r = 0, len(nums)-1
        
        while l < r:
            m = (l+r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l

        right_portion = bfs(nums, pivot, len(nums)-1, target) 

        if right_portion == -1:
            return bfs(nums, 0, pivot, target)
        else:
            return right_portion

         

        