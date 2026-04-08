class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -=1
        curr_time = self.time
        self.tweetMap[userId].append([curr_time, tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        #get user and followers
        relevant_ids = list(set([userId] + list(self.following[userId])))
        res = []

        for uid in relevant_ids:
            if self.tweetMap[uid]:
                index = len(self.tweetMap[uid])-1
                curr_time, tweetId = self.tweetMap[uid][index]
                heapq.heappush(min_heap, [curr_time, tweetId, uid, index-1])
        
        while len(res) < 10 and min_heap:
            curr_time, tweetId, uid, index = heapq.heappop(min_heap)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweetMap[uid][index]
                heapq.heappush(min_heap, [count, tweetId, uid, index-1])

        return res
            
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
