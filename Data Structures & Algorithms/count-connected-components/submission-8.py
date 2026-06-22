class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dict = {}

        for i in range(n):
            dict[i] = None
        
        for e in edges:
            key1, key2 = e[0], e[1]

            while dict[key1] is not None:
                key1 = dict[key1]

            while dict[key2] is not None:
                key2 = dict[key2]

            if key1 != key2:
                dict[key2] = key1
        
        cnt = 0
        for x in dict:
            if dict[x] == None:
                cnt += 1

        return cnt
