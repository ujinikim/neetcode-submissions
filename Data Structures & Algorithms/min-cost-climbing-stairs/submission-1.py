class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [float("inf")] * (n+1)
        dp[0] = dp[1] = 0

        if n <= 1:
            return 0

        for i in range(2, n+1):
            min_cost = min(cost[i-1] + dp[i-1], cost[i-2] + dp[i-2])
            dp[i] = min_cost

        return dp[n]