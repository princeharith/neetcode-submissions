class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #what is the SPACE COMPLEXITY?

        #     prerequisites = [[0,1],[1,2]]

        #  2 -> 1 -> 0

        #  [2,1,0]

        #if all prereqs good and visited
            #add to our list

        #prerequisites = [[0,1],[1,2]]
        # {0: [1],
        #  1: [2]
        #  2: [0]
        # }
        #dfs(0)
        #cycle = {}
        #visited = {0,1,2}
        #course_order = [2,1,1]
            #dfs(1) -> TRUE
            #visited = {1,2}
            #course_order = [2,1]
            #cycle = {0}
                #dfs(2) 
                #cycle = {0,1,2}
                #visited = {}
                #course_order = []
                    #dfs(0)
                    #cycle = {0,1,2}
                    #

        adj_list = defaultdict(list)
        for course, pre in prerequisites:
            adj_list[course].append(pre)
        
        visited = set()
        cycle = set()
        course_order = [] #our result

        def dfs(course):
            if course in visited:
                return True
            if course in cycle:
                return False

            cycle.add(course)
            for prereq in adj_list[course]:
                if not dfs(prereq):
                    return False

            cycle.remove(course)
            visited.add(course)
            course_order.append(course)
            return True



         
        for course in range(numCourses):
            if course not in visited:
                if not dfs(course):
                    return []
        
        return course_order


        