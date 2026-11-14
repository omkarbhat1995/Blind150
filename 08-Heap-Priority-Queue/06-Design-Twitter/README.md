# Design Twitter

**Difficulty:** Medium
**Category:** Heap / Priority Queue / Hash Map

## Problem Description
Implement a simplified version of Twitter which allows users to post tweets, follow/unfollow each other, and view the 10 most recent tweets within their own news feed.

Users and tweets are uniquely identified by their IDs (integers).

Implement the following methods:
* `Twitter()`: Initializes the twitter object.
* `void postTweet(int userId, int tweetId)`: Publish a new tweet with ID `tweetId` by the user `userId`. You may assume that each `tweetId` is unique.
* `List<Integer> getNewsFeed(int userId)`: Fetches at most the 10 most recent tweet IDs in the user's news feed. Each item must be posted by users who the user is following or by the user themself. Tweets IDs should be ordered from most recent to least recent.
* `void follow(int followerId, int followeeId)`: The user with ID `followerId` follows the user with ID `followeeId`.
* `void unfollow(int followerId, int followeeId)`: The user with ID `followerId` unfollows the user with ID `followeeId`.
---
**Example 1:**
```text
Input: ["Twitter", "postTweet", [1, 10], "postTweet", [2, 20], "getNewsFeed", [1], "getNewsFeed", [2], "follow", [1, 2], "getNewsFeed", [1], "getNewsFeed", [2], "unfollow", [1, 2], "getNewsFeed", [1]]

Output: [null, null, null, [10], [20], null, [20, 10], [20], null, [10]]
```
---
## Complexity Analysis   
* Time Complexity:   
    - postTweet, follow, unfollow: $\mathcal{O}(1)$ operations utilizing Hash Maps and Hash Sets.   
    - getNewsFeed: $\mathcal{O}(F) + \mathcal{O}(10 \log F)$ where $F$ is the number of users the current user follows. 
    - Initializing the heap takes $\mathcal{O}(F)$ time, and we extract/insert at most 10 times, taking $\mathcal{O}(\log F)$ per operation.   
* Space Complexity: $\mathcal{O}(T + U \cdot F)$ where $T$ is the total number of tweets, $U$ is the number of users, and $F$ is the average number of followees per user.   
---

## 🧪 Running the Tests

To run the tests for this specific problem, execute the following command in your terminal from the root directory:
```bash
`pytest 01-Arrays-and-Hashing/07-Product-of-Array-Except-Self/test_solution.py -v`
```