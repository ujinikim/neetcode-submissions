class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            if (n > 0):
                return x * self.myPow(x, n - 1)
        
        res = helper(x, abs(n))
        return res if n >= 0 else 1/res