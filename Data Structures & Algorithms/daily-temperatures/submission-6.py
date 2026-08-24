class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i,x in enumerate(temperatures):
            #print(stack)
            while stack and temperatures[i] > temperatures[stack[-1][0]]:
                j = stack.pop()[0]
                result[j] = i-j
            stack.append([i,x])
        return result