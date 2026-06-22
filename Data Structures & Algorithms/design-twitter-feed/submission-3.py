from collections import defaultdict
import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)      # userId -> [(time, tweetId)]
        self.following = defaultdict(set)    # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1   # smaller time = more recent

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        heap = []

        self.following[userId].add(userId)

        for followeeId in self.following[userId]:
            if not self.tweets[followeeId]:
                continue

            last_index = len(self.tweets[followeeId]) - 1
            time, tweetId = self.tweets[followeeId][last_index]

            heapq.heappush(heap, (time, tweetId, followeeId, last_index - 1))

        while heap and len(feed) < 10:
            time, tweetId, followeeId, next_index = heapq.heappop(heap)

            feed.append(tweetId)

            if next_index >= 0:
                next_time, next_tweetId = self.tweets[followeeId][next_index]
                heapq.heappush(
                    heap,
                    (next_time, next_tweetId, followeeId, next_index - 1)
                )

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)