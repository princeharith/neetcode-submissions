class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freqs = collections.Counter(tasks)
        max_heap = [(-v,k) for k,v in task_freqs.items()]

        curr_time = -1
        res = []
        cooldown_list = []
        num_tasks = 0

        i = 0
        while max_heap or cooldown_list:
            print(f'the heap is {max_heap}')
            print(f'cooldown list is {cooldown_list}')
            print(f'curr time is {curr_time}')
            num_tasks += 1
            curr_time += 1
            
            new_cool = []
            for freq, task, cool in cooldown_list:
                if curr_time > cool:
                    heapq.heappush(max_heap, (freq, task))
                else:
                    new_cool.append((freq, task, cool))
            cooldown_list = new_cool

            print(f'the new cooldown is {cooldown_list}')
            print(f'the heap is {max_heap}')

        

            if not max_heap:
                continue

            freq, task = heapq.heappop(max_heap)

            cooldown_time = curr_time + n
            new_frequency = freq + 1

            if new_frequency < 0:
                cooldown_list.append((new_frequency, task, cooldown_time))
            
            


        return num_tasks
        







        