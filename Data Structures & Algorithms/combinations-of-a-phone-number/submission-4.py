class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i, save):
            if i == len(digits):
                res.append(save)
                return 

            for letter in mapping[digits[i]]:
                dfs(i+1, save + letter)
        dfs(0, "")
        return res if len(digits) > 0 else []