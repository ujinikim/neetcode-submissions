class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        mostFreq = cnt.most_common()[0][1]
        numRows = (n + 1) * (mostFreq - 1)
        leftOver = sum([1 for count in cnt.values() if count == mostFreq])
        return max(len(tasks), numRows + leftOver)