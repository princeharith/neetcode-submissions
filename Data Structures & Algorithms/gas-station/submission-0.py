class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #check if sum of gas is more than the sum of cost, if so we have a sol'n
        if sum(gas) < sum(cost):
            return -1

        #we need a string of positive numbers, so we loop around...
        curr_gas = 0
        res = 0
        for i in range(len(gas)):
            curr_gas += (gas[i]-cost[i])
            if curr_gas < 0:
                res = i + 1
                curr_gas = 0
        
        return res
        
        