class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        mostFreq = cnt.most_common()[0][1]
        numRows = (n + 1) * (mostFreq - 1)
        leftOver = sum([1 for count in cnt.values() if count == mostFreq])
        print(numRows)
        print(leftOver)
        # max(len(tasks), (maxFreq - 1) * (n + 1) + maxFreqTaskCount)
        return max(len(tasks), numRows + leftOver)