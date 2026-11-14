import pytest
from solution import Twitter

@pytest.mark.parametrize("commands, args, expected", [
    # --- 1. Standard LeetCode Example ---
    (
        ["Twitter", "postTweet", "postTweet", "getNewsFeed", "getNewsFeed", "follow", "getNewsFeed", "getNewsFeed", "unfollow", "getNewsFeed"],
        [[], [1, 10], [2, 20], [1], [2], [1, 2], [1], [2], [1, 2], [1]],
        [None, None, None, [10], [20], None, [20, 10], [20], None, [10]]
    ),

    # --- 2. Single User > 10 Tweets (Truncation Limit) ---
    (
        ["Twitter"] + ["postTweet"] * 12 + ["getNewsFeed"],
        [[]] + [[1, i] for i in range(1, 13)] + [[1]],
        [None] + [None] * 12 + [[12, 11, 10, 9, 8, 7, 6, 5, 4, 3]]
    ),

    # --- 3. Followee has no tweets ---
    (
        ["Twitter", "follow", "getNewsFeed"],
        [[], [1, 2], [1]],
        [None, None, []]
    ),

    # --- 4. Unfollowing someone you don't follow ---
    (
        ["Twitter", "unfollow", "getNewsFeed"],
        [[], [1, 2], [1]],
        [None, None, []]
    ),

    # --- 5. Attempting to unfollow self ---
    # The news feed should still pull the user's own tweets regardless
    (
        ["Twitter", "postTweet", "unfollow", "getNewsFeed"],
        [[], [1, 55], [1, 1], [1]],
        [None, None, None, [55]]
    ),

    # --- 6. Non-Transitive Following (A follows B, B follows C) ---
    # A should NOT see C's tweets.
    (
        ["Twitter", "postTweet", "postTweet", "follow", "follow", "getNewsFeed"],
        [[], [2, 200], [3, 300], [1, 2], [2, 3], [1]],
        [None, None, None, None, None, [200]]
    ),

    # --- 7. Follower sees old tweets after following ---
    (
        ["Twitter", "postTweet", "follow", "getNewsFeed"],
        [[], [2, 99], [1, 2], [1]],
        [None, None, None, [99]]
    ),

    # --- 8. Feed dynamically updates after unfollow ---
    (
        ["Twitter", "postTweet", "follow", "getNewsFeed", "unfollow", "getNewsFeed"],
        [[], [2, 99], [1, 2], [1], [1, 2], [1]],
        [None, None, None, [99], None, []]
    ),

    # --- 9. Duplicate follows handled gracefully ---
    (
        ["Twitter", "follow", "follow", "postTweet", "getNewsFeed"],
        [[], [1, 2], [1, 2], [2, 10], [1]],
        [None, None, None, None, [10]]
    ),

    # --- 10. Interleaved Timeline across 3 users ---
    (
        ["Twitter", "follow", "follow", "postTweet", "postTweet", "postTweet", "getNewsFeed"],
        [[], [1, 2], [1, 3], [1, 10], [2, 20], [3, 30], [1]],
        [None, None, None, None, None, None, [30, 20, 10]]
    ),

    # --- 11. Maximum Constraint Boundaries ---
    (
        ["Twitter", "postTweet", "getNewsFeed"],
        [[], [500, 10000], [500]],
        [None, None, [10000]]
    ),

    # --- 12. Mutual Followers ---
    (
        ["Twitter", "follow", "follow", "postTweet", "postTweet", "getNewsFeed", "getNewsFeed"],
        [[], [1, 2], [2, 1], [1, 101], [2, 202], [1], [2]],
        [None, None, None, None, None, [202, 101], [202, 101]]
    ),

    # --- 13. Empty Feed Request ---
    (
        ["Twitter", "getNewsFeed"],
        [[], [1]],
        [None, []]
    ),

    # --- 14. Extensive Timeline Merge (Merge K Sorted Lists test) ---
    (
        ["Twitter", "follow", "follow", "follow"] + ["postTweet"]*6 + ["getNewsFeed"],
        [[], [1, 2], [1, 3], [1, 4], [2, 21], [3, 31], [4, 41], [2, 22], [3, 32], [4, 42], [1]],
        [None, None, None, None, None, None, None, None, None, None, [42, 32, 22, 41, 31, 21]]
    ),

    # --- 15. User explicitly follows self ---
    (
        ["Twitter", "follow", "postTweet", "getNewsFeed"],
        [[], [1, 1], [1, 77], [1]],
        [None, None, None, [77]]
    ),
])
def test_twitter(commands, args, expected):
    """
    Simulates the class design inputs to evaluate object state, mimicking LeetCode's execution style.
    """
    twitter_obj = None
    output = []
    
    for cmd, arg in zip(commands, args):
        if cmd == "Twitter":
            twitter_obj = Twitter()
            output.append(None)
        elif cmd == "postTweet":
            output.append(twitter_obj.postTweet(arg[0], arg[1]))
        elif cmd == "getNewsFeed":
            output.append(twitter_obj.getNewsFeed(arg[0]))
        elif cmd == "follow":
            output.append(twitter_obj.follow(arg[0], arg[1]))
        elif cmd == "unfollow":
            output.append(twitter_obj.unfollow(arg[0], arg[1]))
            
    assert output == expected