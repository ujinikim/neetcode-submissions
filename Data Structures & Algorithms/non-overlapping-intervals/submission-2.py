class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        cnt = 0
        start = 0
        end = -1e99
        for itv in intervals:
            if itv[0] < end:
                cnt += 1
                end = itv[1] if itv[1] < end else end
            else:
                end = itv[1]

        return cnt