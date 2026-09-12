class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0

        for i in range(len(nums)):
            if i > furthest:
                return False
            furthest = max(furthest, nums[i]+i)

            if furthest >= len(nums) - 1:
                return True
        
        return False

