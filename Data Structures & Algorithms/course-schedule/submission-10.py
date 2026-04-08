class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_to_prereqs = defaultdict(list)
        for course, prereq in prerequisites:
            course_to_prereqs[course].append(prereq)
        
        visited = set()
        
        def dfs(course):
            if course in visited:
                return False
            visited.add(course)

            for prereq in course_to_prereqs[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            return True
        
        possible = True
        for course in range(numCourses-1):
            if not dfs(course):
                possible = False
        
        return possible
