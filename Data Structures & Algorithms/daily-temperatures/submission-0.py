class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        mono = []
        result = [0] * len(temperatures)
        
        for index, temp in enumerate(temperatures):
            if len(mono) == 0:
                mono.append((index, temp))

            elif mono[-1][1] >= temp:
                mono.append((index, temp))

            else:
                while len(mono) > 0 and mono[-1][1] < temp:
                    idx, item = mono.pop()
                    result[idx] = index-idx

                mono.append((index, temp))

        while mono:
            idx, item = mono.pop()
            result[idx] = 0

        return result