class Twitter:

    def __init__(self):
        self.users = {}
        self.tweets = []
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.addUser(userId)
        curr_time = self.time
        #each tweet has userId and tweetId
        self.tweets.append((userId, tweetId, curr_time))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        print('got news feed')
        feedIds = set([userId] + list(self.users[userId]['following']))

        res = []
        tweet_stack = []

        for tweet in self.tweets:
            uid, tid, curr_time = tweet
            if uid in feedIds:
                tweet_stack.append(tid)

        i = 0
        while i < 10:
            if not tweet_stack:
                break 
            res.append(tweet_stack.pop())
            i += 1
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.addUser(followerId)
        self.addUser(followeeId)
        #'followerId' adds a diff user to their following
        self.users[followerId]['following'].add(followeeId)

        #'followindId' adds a diff user to their followers
        self.users[followeeId]['followers'].add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.addUser(followerId)
        self.addUser(followeeId)

        #user 'followerId' no longer has folowee in his following
        #check if this user is in the following
        if followeeId in self.users[followerId]['following']:
            self.users[followerId]['following'].remove(followeeId)

        #the followee loses a follower
        if followerId in self.users[followeeId]:
            self.users[followeeId]['followers'].remove(followerId)
    
    def addUser(self, userId):
        if userId not in self.users:
            self.users[userId] = {"following": set(), "followers": set()}

        
