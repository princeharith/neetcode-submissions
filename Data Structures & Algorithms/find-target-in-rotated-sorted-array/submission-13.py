class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find the pivot (smallest element)
        #binary search from pivot, end of array
        #binary search from start of array, to pivot
        
        def find_pivot(nums: List[int]) -> int:
            l, r = 0, len(nums)-1
            while l < r:
                mid = (l+r)//2
                if nums[mid] < nums[r]:
                    r = mid
                else:
                    l = mid + 1
            return l
        
        def bin_search(l, r) -> int:
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        
        pivot = find_pivot(nums)
        result = bin_search(0, pivot)

 
        
        if bin_search(0, pivot) != -1:
            return result
        else:
            return bin_search(pivot, len(nums)-1)

        
        
        