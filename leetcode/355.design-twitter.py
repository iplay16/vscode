#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#
#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#
import tools
from typing import List
import collections
class Twitter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets_cnt = 0
        self.tweets = collections.defaultdict(list)
        self.follower_ship = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        # self.tweets[userId].append([tweetId, self.tweets_cnt])
        self.tweets[userId].insert(0,[tweetId, self.tweets_cnt])
        self.tweets_cnt += 1

    def getNewsFeed(self, userId:int) -> List[int]:

        #version 2##################################################
        followuserset=self.follower_ship[userId]
        followuserset.add(userId)
        indexdict=collections.defaultdict(int)
        recentlist=[]
        # record the user who posted last tweet 
        userflag=None
        maxtime=-1
        for i in range(10):
            if not followuserset:
                break
            #########core###############
            maxtime=-1
            for user in followuserset:   #n 为第n位followuser
                if not self.tweets[user]:
                    continue
                usertweetlist=self.tweets[user] #one of user's tweets list
                if len(usertweetlist)==indexdict[user]:
                    continue
                if maxtime<usertweetlist[indexdict[user]][1]:
                    maxtime=usertweetlist[indexdict[user]][1]
                    userflag=user
            if maxtime==-1:
                continue
            usertweetlist=self.tweets[userflag]
            recentlist.append(usertweetlist[indexdict[userflag]][0])
            indexdict[userflag]=indexdict[userflag]+1
            ##############
        return recentlist
        ############################################



        # for user in self.follwer_ship[userId]://获取关注用户
        #     for tweetitem in self.tweets[user]:
        #         scnt=tweetitem[1]


        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        # recent_tweets = []
        # user_list = list(self.follower_ship[userId]) + [userId]
        # userId_tweet_index = [[userId, len(self.tweets[userId]) - 1] for userId in user_list if userId in self.tweets]

        # for _ in range(10):
        #     max_index = max_tweet_id = max_user_id = -1
        #     for i, (user_id, tweet_index) in enumerate(userId_tweet_index):
        #         if tweet_index >= 0:
        #             tweet_info = self.tweets[user_id][tweet_index]
        #             if tweet_info[1] > max_tweet_id:
        #                 max_index, max_tweet_id, max_user_id = i, tweet_info[1], user_id

        #     if max_index < 0: break
        #     recent_tweets.append(self.tweets[max_user_id][userId_tweet_index[max_index][1]][0])
        #     userId_tweet_index[max_index][1] -= 1

        # return recent_tweets

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId != followeeId:
            self.follower_ship[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.follower_ship and followeeId in self.follower_ship[followerId]:
            self.follower_ship[followerId].remove(followeeId)      


if __name__=='__main__':
    t=Twitter()
    # action=["Twitter","postTweet","getNewsFeed"]
    # data=[[],[1,5],[1]]
    # action=["Twitter","postTweet","getNewsFeed"]
    # data=[[],[1,5],[1]]
    # action=["Twitter","follow","getNewsFeed"]
    # data=[[],[1,5],[1]]
    # action=["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]
    # data=[[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]
    # action=["Twitter","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","getNewsFeed","follow","getNewsFeed"]
    # data=[[],[2,5],[1,3],[1,101],[2,13],[2,10],[1,2],[2,94],[2,505],[1,333],[1,22],[2],[2,1],[2]]
    # action=["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]
    # data=[[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]
    

    action=["Twitter","postTweet","follow","follow","getNewsFeed"]
    data=[[],[2,5],[1,2],[1,2],[1]]
    print(action[1:])
    print(data[1:])
    l=tools.runTest(t,action,data)
    print(l)
    e=[None,None,None,None,[5]]
    e.pop(0)
    print(e)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

