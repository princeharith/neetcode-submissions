class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        indegree = [0] * numCourses
        for course,pre in prerequisites:
            #course -> pre
            indegree[pre] += 1
            adj_list[course].append(pre)
        
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        numProcessed = 0
        output = []
        while q:
            numProcessed += 1
            node = q.popleft()
            output.append(node)

            for prereq in adj_list[node]:
                indegree[prereq] -= 1

                if indegree[prereq] == 0:
                    q.append(prereq)
        
        if numProcessed != numCourses:
            return []
        return output[::-1]

            
        
        
