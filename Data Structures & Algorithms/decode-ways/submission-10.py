class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        two_ago = 1
        one_ago = 1
        count = 0
        for c in range(1, len(s)):

            if s[c] != "0":
                count += one_ago
            if 10 <= int(s[c-1:c+1]) <= 26:
                count += two_ago

            count, one_ago, two_ago = 0, count, one_ago
        
        return one_ago
            