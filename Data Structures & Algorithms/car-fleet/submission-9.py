class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = sorted(list(zip(position, speed)), reverse=True)
        bottleneck = 0
        car_fleets = 0

        for p, s in pos_speed:
            ttd = (target-p) / s

            if ttd > bottleneck:
                car_fleets += 1
                bottleneck = ttd
        return car_fleets

        
        
        # pos_speed = list(zip(position, speed))
        # pos_speed = sorted(pos_speed, reverse=True)
        # print(pos_speed)
        # stack = []
        # for p, s in pos_speed:
        #     ttd = (target - p) / s
        #     stack.append(ttd)

        #     if len(stack) >= 2 and stack[-1] <= stack[-2]:
        #         stack.pop()

        # return len(stack)


