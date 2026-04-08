class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [[temperatures[0], 0]]
        res = [0]*len(temperatures)

        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                idx = stack[-1][1]
                res[idx] = i - idx
                stack.pop()
            if not stack or temperatures[i] <= stack[-1][0]:
                stack.append([temperatures[i], i])
        
        return res
                

            