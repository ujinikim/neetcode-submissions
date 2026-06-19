class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)

        res = []
        temp = set()
        track = 0
        for i in range(len(s)):
            num = s[i]

            if num not in temp:
                temp.add(num)
            count[num] -= 1

            if any(count[num] > 0 for num in temp):
                continue
            
            temp = set()
            res.append(i - track + 1)
            track += i - track + 1

        return res
            
                