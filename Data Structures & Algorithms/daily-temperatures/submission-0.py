class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # Stores pairs of [temp, index]

        for i, t in enumerate(temperatures):
            # While stack has days and current temp is warmer than top of stack
            while stack and t > stack[-1][0]:
                stackTemp, stackIdx = stack.pop()
                res[stackIdx] = i - stackIdx
            
            stack.append([t, i])

        return res