class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        hm = {}

        def dfs(i, amount):
            if amount == 0:
                return 1

            if i == len(coins) or amount < 0:
                return 0

            if (i, amount) in hm:
                return hm[(i, amount)]

            use = dfs(i, amount - coins[i])
            skip = dfs(i + 1, amount)

            hm[(i, amount)] = use + skip
            return hm[(i, amount)]

        return dfs(0, amount)