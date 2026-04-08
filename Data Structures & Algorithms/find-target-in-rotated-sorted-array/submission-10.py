class Solution:
    def search(self, nums: List[int], target: int) -> int: 
        def bin_search(l,r):
            while l <= r:
                print(l,r)
                mid = (l+r)//2
                print(nums[mid])
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        if nums[0] < nums[-1]:
            return bin_search(0, len(nums)-1)

        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
        pivot = r
        print(pivot)
        
        if target > nums[-1]:
            return bin_search(0, pivot-1)
        else:
            return bin_search(pivot, len(nums)-1)
        
        