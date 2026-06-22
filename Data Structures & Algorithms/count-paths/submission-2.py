class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        dp = [[0 for _ in range(m)] for _ in range(n)]
        # matrix = [[initial_value for _ in range(cols)] for _ in range(rows)]
        
        dp[-1] = [1 for _ in range(m)]
        for r in range(n):
            dp[r][-1] = 1



        for x in range(n - 2, -1, -1):
            for y in range(m - 2, -1, -1):
                print(x, 'x')
                print(y, 'y')
                dp[x][y] = dp[x+1][y] + dp[x][y+1]
        

        return dp[0][0]