class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * m
        for x in range(n - 2, -1, -1):
            for y in range(m - 2, -1, -1):
                print(x, 'x')
                print(y, 'y')
                dp[y] += dp [y+1] 
        

        return dp[0]