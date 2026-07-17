class Solution:
    def climbStairs(self, n: int) -> int:
        # 0 1 2 3 4 N Stair 
        # 0 1 2 3 5 Ways

        # 4 - [1, 1, 1, 1] [1, 1, 2] [1, 2, 1] [2, 1, 1] [2 2]

        if n == 0 or n == 1:
            return n
        twoAgo = 1
        oneAgo = 1
        total = 0
        for i in range(1, n):
            total = twoAgo + oneAgo
            twoAgo = oneAgo
            oneAgo = total

        return total
            



