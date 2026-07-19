class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1m = sorted(s1)
        hs = set([s for s in s1])
        for i in range(len(s2)-len(s1m)+1):
            print(i)
            if s2[i] in hs:
                new = sorted(s2[i:i+len(s1)])
                if new == s1m:
                    return True
        return False

            