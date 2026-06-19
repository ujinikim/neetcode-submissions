class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 0 to N
        sum = 0
        sumLoc = 0
        for i in range(len(nums)+1):
            print(i)
            sumLoc += i
        for i, n in enumerate(nums):
            sum += n
        print(sumLoc)
        return sumLoc - sum
