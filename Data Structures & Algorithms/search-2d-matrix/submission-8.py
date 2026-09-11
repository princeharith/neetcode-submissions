class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        #figure out which row it is in
            #if its less than row[0], row is too big. Go up 
            #if its greater than row[-1], row is too small, go down
            #otherwise, binary search this row

        #then, run binary search on the row
        def binary_search(row: List[int]) -> bool:
            l, r = 0, len(row)-1
            while l <= r:
                mid = (l+r)//2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False
   
        top, bottom = 0, len(matrix)-1
        while top <= bottom:
            mid = (top+bottom)//2
            curr_row = matrix[mid]
            if target < curr_row[0]:
                bottom = mid - 1
            elif target > curr_row[-1]:
                top = mid + 1
            else:
                return binary_search(curr_row)
        
        return False

