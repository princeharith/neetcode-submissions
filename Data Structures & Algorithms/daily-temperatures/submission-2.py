class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # temperatures = [30,38,30,36,35,40,28]
        
        # res = [0,0,0,0,0,0,0]

        # stack = [(0, 30),]


        res = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                og_index, _ = stack.pop()
                res[og_index] = idx - og_index

            stack.append((idx, temp))
            print(stack)

        return res