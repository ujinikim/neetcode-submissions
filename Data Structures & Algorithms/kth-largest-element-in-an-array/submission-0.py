class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mh = [-x for x in nums]
        print(mh)
        heapq.heapify(mh)
        for _ in range(k-1):
            heapq.heappop(mh)
        
        return -heapq.heappop(mh)

