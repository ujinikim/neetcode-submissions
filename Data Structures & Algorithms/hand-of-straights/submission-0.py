from typing import List
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counts = Counter(hand)

        while counts:
            smallest = min(counts)

            for num in range(smallest, smallest + groupSize):
                if counts[num] == 0:
                    return False

                counts[num] -= 1

                if counts[num] == 0:
                    del counts[num]

        return True