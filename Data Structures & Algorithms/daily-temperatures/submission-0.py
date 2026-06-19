class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lst = []
        for i, temp in enumerate(temperatures):
            curTemp = temp
            for j in range(i+1, len(temperatures)):
                if curTemp < temperatures[j]:
                    lst.append(j - i)
                    break
            else:
                lst.append(0)
        return lst