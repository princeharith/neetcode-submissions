class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [-val for val in counts.values()]
        heapq.heapify(heap)

        #remaining_count, next available time
        q = deque()

        time = 0
        while heap or q:
            time += 1
            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        return time




        
        
        # current_time = 0

        # {
        #     X: 0
        #     Y: 2
        # }

        # #current_time + n
        # cooldown_queue: [(3, Y)]

        #check our heap
        #if we can use, pop from heap
        #to check if we can use -> heap[0][0] <= curr_time
            #decrease the count
            #if count > 0, add back to heap, at curr_time + n
            #do this until heap is empty
        
        #Cycle 0: X
        #Cycle 1: Y
        #Cycle 2: X
        #Cycle 3: Y
    
