class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        #sort by position, need both together
        pos_speed = [(position, speed) for position, speed in zip(position, speed)]
        pos_speed = sorted(pos_speed, key=lambda x: x[0])
        
        stack = []
        for pos, speed in reversed(pos_speed):
            #check if the current ttd
            ttd = (target-pos)/speed
            if stack and ttd <= stack[-1]:
                continue
            else:
                stack.append(ttd)
        

        return len(stack)
        


        #   ttd=8      ttd=3
        # <----------------------------------->
        #                                ttd=2
        #                   ttd=1

        
        