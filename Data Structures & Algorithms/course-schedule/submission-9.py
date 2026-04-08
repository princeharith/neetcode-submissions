class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_to_prereqs = defaultdict(list)
        for course, prereq in prerequisites:
            course_to_prereqs[course].append(prereq)
        
        
        def dfs(course, visited):
            if course in visited:
                return False
            visited.add(course)

            for prereq in course_to_prereqs[course]:
                if not dfs(prereq, visited):
                    return False
            visited.remove(course)
            return True
        
        possible = True
        for course in range(numCourses-1):
            visited = set()
            if not dfs(course, visited):
                possible = False
        
        return possible
