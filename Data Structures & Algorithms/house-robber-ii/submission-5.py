class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(start, end):
            memo = {}

            def dfs(i):
                if i > end:
                    return 0

                if i in memo:
                    return memo[i]

                skip = dfs(i + 1)
                rob = nums[i] + dfs(i + 2)

                memo[i] = max(skip, rob)
                return memo[i]

            return dfs(start)

        return max(
            rob_line(0, len(nums) - 2),  # exclude last
            rob_line(1, len(nums) - 1)   # exclude first
        )

        