class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bin_search(l,r,target, nums):
            while l <= r:
                middle = (l+r)//2
                if nums[middle] == target:
                    return True
                elif nums[middle] < target:
                    l += 1
                else:
                    r -= 1
            return False
        
        top, bottom = 0, len(matrix)-1
        times_ran = 0
        while top <= bottom:
            print(top, bottom)
            middle_row = matrix[(top+bottom)//2]
            print(middle_row)
            if middle_row[0] <= target <= middle_row[-1]:
                print('doing bin_search')
                return bin_search(0, len(middle_row)-1, target, middle_row)
            elif middle_row[0] < target and middle_row[-1] < target:
                top += 1
            else:
                bottom -=1
            times_ran += 1
        return False
            
        

