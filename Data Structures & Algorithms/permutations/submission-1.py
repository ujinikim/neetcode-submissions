class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur, remaining):
            if not remaining:
                res.append(cur)
                return

            for i, x in enumerate(remaining):
                dfs(
                    cur + [x],
                    remaining[:i] + remaining[i + 1:]
                )

        dfs([], nums)
        return res