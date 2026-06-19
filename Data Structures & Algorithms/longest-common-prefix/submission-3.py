class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        numShorts = 999
        for s in strs:
            if len(s) < numShorts:
                numShorts = len(s)
        print(numShorts)
        res = ""
        for i in range(numShorts):
            c = strs[0][i]
            for s in strs:
                if c != s[i]:
                    return res
            res += s[i]
        return res
                