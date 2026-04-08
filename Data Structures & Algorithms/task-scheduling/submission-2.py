class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #we first get the frequencies/counts
        #then we add to our max heap
        
        #while we have a heap and coooldown list...
        #we pop the max frequency
        #cooldown list will look like (frequency, available_cycle, task)

        #if current_cycle >= available_cycle, we push back onto heap with new frequency
        #otherwise, we add to our new cooldown list to prevent removing while iterating
        #set cooldown to our new cooldown

        counts = collections.Counter(tasks)
        max_heap = [(-count, task) for task,count in counts.items()]
        heapq.heapify(max_heap)
        cooldown_list = []
        num_cycles = 0

        while max_heap or cooldown_list:
            num_cycles += 1

            new_cooldown = []
            for count, available_cycle, task in cooldown_list:
                if num_cycles >= available_cycle:
                    #count is positive, so we add the negative to maintain max_heap structure
                    heapq.heappush(max_heap, (-count, task))
                else:
                    new_cooldown.append((count, available_cycle, task))
            cooldown_list = new_cooldown
            #count is negative at this point, so we flip to positive
            if not max_heap:
                continue
            count, task = heapq.heappop(max_heap) 
            count = -count

            if count > 1:
                cooldown_list.append((count-1, num_cycles+n+1, task))
        
        return num_cycles
