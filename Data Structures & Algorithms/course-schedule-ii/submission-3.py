class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #topological sort
        adj_list = defaultdict(list)
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        visiting, visit = set(), set()
        output = []
        def dfs(course):
            if course in visiting:
                return False
            if course in visit:
                return True

            visiting.add(course)

            for prereq in adj_list[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)

            visit.add(course)
            output.append(course)
            return True
            


        
        res = []
        #loop through courses
        for course in range(numCourses):
            #run dfs on each course, add to our set
            if not dfs(course):
                return []
        
    
        return output


