class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dict = {}
        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if (i, j) in dict:
                return dict[(i, j)]
            
            highest = 0
            if text1[i] == text2[j]:
                highest = 1 + dfs(i+1, j+1)
            else:
                highest = max(dfs(i+1, j), dfs(i, j+1))
            
            dict[(i, j)] = highest

            return highest


        return dfs(0, 0)