class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #adj_list = {course:prereq for course,prereq in prerequisites}
        adj_list = defaultdict(list)
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        visited = set()
        cycle = set()


        #visited = set(0,1,2)
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for prereq in adj_list[course]:
                if not dfs(prereq):
                    return False
            cycle.remove(course)
            visited.add(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True


        # [0,1], [1,2]

    