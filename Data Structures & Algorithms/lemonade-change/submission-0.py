class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = [0,0,0]
        #each index corresponds to number of 5, 10, 20

        for bill in bills:
            if bill == 5:
                change[0] += 1
            elif bill == 10:
                change[0] -= 1
                change[1] += 1
            elif bill == 20:
                #we wither give a 10 and a 5 
                if change[1] > 0:
                    change[1] -= 1
                    change[0] -= 1
                #or 3 5s
                else:
                    change[0] -= 3
                
            if change[0] < 0:
                return False
        
        return True

                #or 3 5s


                 
        