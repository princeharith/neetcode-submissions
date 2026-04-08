class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sorted_tasks = [(enque, process, idx) for idx, (enque, process) in enumerate(tasks)]
        sorted_tasks.sort()

        minHeap = []
        curr_time = 0
        curr_idx = 0

        res = []

        while curr_idx < len(sorted_tasks) or minHeap:
            while curr_idx < len(sorted_tasks) and curr_time >= sorted_tasks[curr_idx][0]:
                process_time = sorted_tasks[curr_idx][1]
                index = sorted_tasks[curr_idx][2]
                heapq.heappush(minHeap, (process_time, index))
                curr_idx += 1
            
            if not minHeap:
                curr_time = sorted_tasks[curr_idx][0]
                continue
            
            process_time, index = heapq.heappop(minHeap)
            res.append(index)
            curr_time += process_time
        
        return res

        