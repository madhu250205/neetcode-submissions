from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetId]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Decrement count so we can use Python's min-heap as a max-heap chronologically
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # Ensure a user always follows themselves to see their own tweets
        self.followMap[userId].add(userId)

        # Gather the most recent tweet from each followee
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])

        heapq.heapify(minHeap)

        # Extract up to the 10 most recent tweets
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, userId: int, followeeId: int) -> None:
        self.followMap[userId].add(followeeId)

    def unfollow(self, userId: int, followeeId: int) -> None:
        if followeeId in self.followMap[userId]:
            self.followMap[userId].remove(followeeId)