class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # majority = nums[0]
        # prev = nums[0]
        # cnt = 0
        # curCnt = 0
        # for num in nums:
        #     if prev == num:
        #         curCnt += 1
        #         if curCnt > cnt:
        #             majority = num
        #             cnt = curCnt
        #     else:
        #         curCnt = 1
        #     prev = num
        # return majority

        #Linear time Solution
        cand = 0
        cnt = 0

        for num in nums:
            if cnt == 0:
                cand = num
            
            cnt += (1 if cand == num else -1)
        
        return cand

            
            