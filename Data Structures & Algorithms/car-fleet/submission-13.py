class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # position = [4,1,0,7]
        # speed = [2,2,1,1]
        # time  = [3,5,10,3]

        #sort by positions
        # [7,4,1,0]

        #push their times onto the stack
            #if farther position but shorter time, becomes a fleet (keep slowes)
        # [3,5,  10]

        stack = []
        #stack = []
        #whats the time xomplexity of below
        pos_speed = [(pos, speed) for pos, speed in zip(position, speed)]
        pos_speed.sort(reverse=True)

        #ttd = 3
        # stack = [3, ]

        for pos,speed in pos_speed:
            # print(target, pos, speed)
            ttd = (target - pos) / (speed)
            # print(stack)
            # print(ttd)
            if stack and stack[-1] >= ttd:
                continue
            stack.append(ttd)

        return len(stack)


        # [8,7,6,5,4,3]
        # [4,4,4,4,4,4]

        # ttd = (2)/4 = 1
        # (10-6)/2 = 4/2

        # stack = [1,2]

        
