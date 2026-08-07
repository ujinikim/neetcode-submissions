from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counts = Counter(hand)

        for start in sorted(counts):
            groups = counts[start]

            if groups > 0:
                for card in range(start, start + groupSize):
                    if counts[card] < groups:
                        return False
                    counts[card] -= groups

        return True