public class Solution {
    public int MaxProfit(int[] prices) {
        if (prices.Length <= 1)
        {
            return 0;
        }
        var profit = 0;
        var min = int.MaxValue;
        for(int i = 0; i < prices.Length; i++)
        {
            if (prices[i] < min)
            {
                min = prices[i];
            }
            else
            {
                var newProfit = prices[i] - min;
                if (newProfit > profit)
                {
                    profit = newProfit;
                }
            }
        }
        return profit;
    }
}
