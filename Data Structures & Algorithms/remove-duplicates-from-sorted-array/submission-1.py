class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uq = sorted(set(nums))
        nums[:] = uq
        return len(uq)