class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        stack.append({'idx': 0, 'temp':temperatures[0]})

        for i in range(1, len(temperatures)):
            while len(stack) != 0 and temperatures[i] > stack[-1]['temp']:
                temp = stack.pop()
                res[temp['idx']] = i - temp['idx']
            stack.append({'idx': i, 'temp':temperatures[i]})
        
        res[-1] = 0
        return res