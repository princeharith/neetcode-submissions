class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #figure out which row to search
        #then, run binary search on that row 

        def bin_search(nums):
            l, r = 0, len(nums)-1
            while l <= r:
                m = (l+r)//2
                if nums[m] == target:
                    return True
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return False

        top, bottom = 0, len(matrix)-1
        while top <= bottom:
            middle = (top+bottom)//2
            if target < matrix[middle][0]:
                bottom = middle - 1
            elif target > matrix[middle][-1]:
                top = middle + 1
            else:
                return bin_search(matrix[middle])
        
        return False
        