class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        memo = {}
        def dfs(i, canRobLastHouse):
            if i >= len(nums):
                return 0

            if (i, canRobLastHouse) in memo:
                return memo[(i, canRobLastHouse)]

            route_1 = dfs(i+1, canRobLastHouse)
            route_2 = 0
            if not i == len(nums)-1 or canRobLastHouse:
                if i == 0:
                    canRobLastHouse = False
                route_2 = nums[i] + dfs(i+2, canRobLastHouse)

            memo[(i, canRobLastHouse)] = max(route_1, route_2)
            return max(route_1, route_2)

            
        return dfs(0, True)

        