class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_fleets = 0
        pos_speed = sorted(list(zip(position, speed)), reverse=True)

        print(pos_speed)

        bottleneck = 0
        for pos,spd in pos_speed:
            dist_to_tgt = target - pos
            time_to_destination = dist_to_tgt/spd
            print(time_to_destination)

            if time_to_destination > bottleneck:
                car_fleets += 1
                bottleneck = time_to_destination
        
        return car_fleets