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
        
        def bin_search(nums: List[int], target: int) -> int:
            l, r = 0, len(nums)-1
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        
        pivot_index = find_pivot(nums)
        first_half_sorted = nums[:pivot_index]
        second_half_sorted = nums[pivot_index:]

        first_half_search = bin_search(first_half_sorted, target)
        second_half_search = bin_search(second_half_sorted, target)

        if first_half_search == -1 and second_half_search == -1:
            return -1
        if first_half_search != -1:
            return first_half_search
        else:
            return second_half_search + pivot_index
        
        
        