class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapq.heapify(self.heap)
        self.k = k 
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        #return top of the heeap
        return self.heap[0]
    
    # ["KthLargest", [3, [3, 3, 3, 5]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]
    

    # ["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]

    # [3,3,5]
    # k = 3

        

        #only keep the heap at size k
        #that way, element is the kth smallest