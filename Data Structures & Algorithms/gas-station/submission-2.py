class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        curr_gas = 0
        starting_idx = 0
        for i in range(len(gas)):
            curr_gas += gas[i]
            curr_gas -= cost[i]
            if curr_gas < 0:
                starting_idx = i + 1
                curr_gas = 0
        
        return starting_idx
        