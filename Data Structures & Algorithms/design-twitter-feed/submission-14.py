class Twitter:

    def __init__(self):
        self.followingMap = defaultdict(set)
        self.twitterMap = defaultdict(list)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        curr_time = self.time
        self.twitterMap[userId].append((curr_time, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        res = []
        relevant_ids = [userId] + list(self.followingMap[userId])
        for uid in relevant_ids:
            index = len(self.twitterMap[uid])-1
            if self.twitterMap[uid]:
                curr_time, tweetId = self.twitterMap[uid][index]
                heapq.heappush(min_heap, [curr_time, tweetId, uid, index-1])
        
        while min_heap and len(res) < 10:
            curr_time, tweetId, uid, index = heapq.heappop(min_heap)
            res.append(tweetId)

            if index >= 0:
                curr_time, tweetId = self.twitterMap[uid][index]
                heapq.heappush(min_heap, [curr_time, tweetId, uid, index-1])
            
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followingMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followingMap[followerId]:
            self.followingMap[followerId].remove(followeeId)
        
