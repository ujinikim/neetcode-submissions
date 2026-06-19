class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 0
        s = len(nums)
        while r < s:
            nums[l] = nums[r]
            while r < s and nums[l] == nums[r]:
                r+=1
            l+=1
        return l
            