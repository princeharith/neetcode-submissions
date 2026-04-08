class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = collections.Counter(tasks)
        #{A: 3, B: 1, C: 1}
        maxHeap = [(-freq, task) for task, freq in freqs.items()]
        heapq.heapify(maxHeap)

        queue = deque()
        #available cycle, frequency, task

        num_cycles = 0
        sim_list = []

        while maxHeap or queue:
            num_cycles += 1

            if queue and num_cycles == queue[0][0]:
                available_cycle, frequency, task = queue.popleft()
                heapq.heappush(maxHeap, (frequency, task))
            
            if not maxHeap:
                sim_list.append('Idle')
                time = queue[0][0]
                continue

            frequency, task = heapq.heappop(maxHeap)
            sim_list.append(task)
            frequency += 1

            if frequency < 0:
                queue.append((num_cycles+n+1, frequency, task))
        
        print(sim_list)
        return num_cycles
