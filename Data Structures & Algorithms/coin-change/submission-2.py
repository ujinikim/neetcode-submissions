class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [1e99] * (amount+1)
        print(memo)
        memo[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    memo[i] = min(memo[i], memo[i-coin] + 1)
        return memo[amount] if memo[amount] < 1e99 else -1