class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            comb = numbers[i] + numbers[j]

            if target < comb:
                j-=1
            elif target > comb:
                i+=1
            else:
                return [i+1, j+1]

        return []