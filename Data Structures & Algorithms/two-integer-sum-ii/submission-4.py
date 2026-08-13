class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #target = 3
        #[1,2,3,4]
        #  x y
        
        #curr_sum = 3
        #return [x+1, y+1]

        p1, p2 = 0, len(numbers)-1

        while p1 < p2:
            curr_sum = numbers[p1] + numbers[p2]
            if curr_sum == target:
                return [p1+1, p2+1]
            elif curr_sum < target:
                p1 += 1
            else:
                p2 -= 1
        
            

        