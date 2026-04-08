class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        #maxHeap
        max_heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]

        heapq.heapify(max_heap)

        #(-3, c)
        #(-1, b)
        #(0, a)

        res = ''

        while max_heap:
            cnt, char = heapq.heappop(max_heap)
        
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not max_heap:
                    break
                #then we need to use the second
                cnt2, char2 = heapq.heappop(max_heap)
                if cnt2 < 0:
                    res += char2
                    cnt2 += 1
                    heapq.heappush(max_heap, (cnt2, char2))
                
                #push the original back in
                heapq.heappush(max_heap, (cnt, char))
            else:
                if cnt < 0:
                    cnt += 1
                    res += char
                    heapq.heappush(max_heap, (cnt, char))
        
        return res
