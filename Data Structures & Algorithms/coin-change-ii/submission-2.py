class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        hm = {}
        def dfs(i, amount):
            if amount == 0:
                return 1

            if i == len(coins) or amount < 0:
                return 0

            total = 0

            # use current coin
            if (i, amount - coins[i]) not in hm: 
                x = dfs(i, amount - coins[i])
                hm[(i, amount - coins[i])] = x
                total += x
            else:
                total += hm[(i, amount - coins[i])]

            # don't use current coin
            total += dfs(i + 1, amount)

            return total

        return dfs(0, amount)