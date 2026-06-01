class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #pick the middle row
            #if number is less than curr_row[0]:
                #exists in 0...curr_row-1
            
            #otherwise if number is greater than curr_row[-1]:
                #exists in curr_row+1, num(rows)
            
            #othwerwise
                #do binary search on this row
        
        def binary_search(row, target):
            l,r = 0, len(row)-1
            while l <= r:
                middle = (l+r)//2
                if row[middle] == target:
                    return True
                if row[middle] < target:
                    l = middle + 1
                else:
                    r = middle - 1
            return False

        num_rows = len(matrix)
        lower, upper = 0, num_rows-1

        while lower <= upper:
            middle = (lower+upper)//2
            if target < matrix[middle][0]:
                upper = middle - 1
            elif target > matrix[middle][-1]:
                lower = middle + 1
            else:
                return binary_search(matrix[middle], target)
        
        return False
        
