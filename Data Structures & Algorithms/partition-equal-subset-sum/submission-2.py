class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        target = int(total / 2)
        dp = [False for _ in range(target+1)]
        dp[0] = True

        for num in nums:
            for x in range(target, num-1, -1):
                dp[x] = dp[x] or dp[x-num]
        return dp[-1]
