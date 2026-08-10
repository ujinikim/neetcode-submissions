class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_list = sorted(intervals)
        offset = sorted_list[0]
        lst = []
        for idx in range(1, len(intervals)):
            
            if sorted_list[idx][0] <= offset[1]:
                offset[1] = max(sorted_list[idx][1], offset[1])
            else:
                lst.append(offset)
                offset = sorted_list[idx]
        
        lst.append(offset)
        return lst


        
        
            
        