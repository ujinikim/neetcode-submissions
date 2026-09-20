class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest_price = prices[0]
        for i in range(1, len(prices)):
            if lowest_price > prices[i]:
                lowest_price = prices[i]
            else:
                res = max(res, prices[i]-lowest_price)
        return res