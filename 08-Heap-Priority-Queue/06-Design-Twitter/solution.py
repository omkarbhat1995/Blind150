from typing import List
from collections import defaultdict
import heapq

class Twitter:
    def __init__(self):
        """
        Initializes the Twitter object.
        Uses a global timestamp to track the absolute order of tweets across all users.
        """
        self.time = 0
        self.tweet_map = defaultdict(list)  # userId -> list of [time, tweetId]
        self.follow_map = defaultdict(set)  # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Publish a new tweet by userId.
        """
        self.tweet_map[userId].append([self.time, tweetId])
        # Decrement time so the most recent tweet has the smallest value for the min-heap[cite: 1]
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Fetches the 10 most recent tweet IDs from the user and their followees.
        """
        res = []
        min_heap = []

        # Ensure the user always sees their own tweets[cite: 1]
        self.follow_map[userId].add(userId)
        
        # Grab the single most recent tweet from each followee to initialize the heap[cite: 1]
        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet_map:
                index = len(self.tweet_map[followeeId]) - 1
                tweet_time, tweetId = self.tweet_map[followeeId][index]
                min_heap.append([tweet_time, tweetId, followeeId, index - 1])
        
        heapq.heapify(min_heap)

        # Merge the k sorted lists to find the 10 absolute most recent tweets[cite: 1]
        while min_heap and len(res) < 10:
            tweet_time, tweetId, followeeId, index = heapq.heappop(min_heap)
            res.append(tweetId)
            
            # If this followee has more tweets, push their next most recent tweet into the heap[cite: 1]
            if index >= 0:
                tweet_time, tweetId = self.tweet_map[followeeId][index]
                heapq.heappush(min_heap, [tweet_time, tweetId, followeeId, index - 1])
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee.
        """
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee.
        """
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)