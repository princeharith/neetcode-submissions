class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #heap to keep track of counts
        counts = Counter(tasks)
        max_heap = [-val for val in counts.values()]
        heapq.heapify(max_heap)
        #cooldown q that tells us the time we can use, remaining count
        q = deque()

        time = 0
        while max_heap or q:
            time += 1
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1
                if cnt:
                    q.append((time+n, cnt))
            if q and q[0][0] == time:
                heapq.heappush(max_heap, q.popleft()[1])
        
        return time


        #if something in our heap (with counts), that means we can pop it. While there is a heap, pop, 
        #lower the count

        #if there is a count, add it to our queue

        #if we have hit a time we can take off the front of the cooldown queue, add to our heap
        