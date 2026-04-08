class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #have something tracking the current time
        #have a minHeap for available tasks (loop through, if curr_time >= enqueueTime, add to heap 
        #- minHeap must be by processing time)

        #pop from heap
        #loop through our remaining tasks list after each iteration, add ot heap as neecessary

        availTasks = tasks
        taskIndexMap = {tuple(val):idx for idx,val in enumerate(tasks)}
        minHeap = []
        res = []

        curr_time = min([task[0] for task in tasks])
        recent_process_time = 0

        #[[5,2],[4,4],[4,1],[2,1],[3,3]]

        while minHeap or availTasks:
            curr_time += recent_process_time

            newTaskList = []
            for task in availTasks:
                if curr_time >= task[0]:
                    #we need the processing time and index
                    index = taskIndexMap[tuple(task)]
                    heapq.heappush(minHeap, (task[1], index))
                else:
                    newTaskList.append(task)
            availTasks = newTaskList

            if not minHeap:
                recent_process_time = 1
                continue
            
            recent_process_time, idx = heapq.heappop(minHeap)
            res.append(idx)
        
        return res




