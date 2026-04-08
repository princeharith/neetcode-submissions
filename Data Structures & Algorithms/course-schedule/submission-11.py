class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # #no prereqs possible
        # 0: [1]
        # 1: [0]


        # prereqs = [[0,1], [0,2], [2,3]]

        #make an adjacency list
            #map courses to their preq w a hashmap
        adj_list = defaultdict(list)
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            
            visited.add(course)
            
            for prereq in adj_list[course]:
                if not dfs(prereq):
                    return False

            visited.remove(course)
            
            return True


        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

       
       
       
        #time: O(n^2) ??
        #space: O(n) ??