class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = {i: [] for i in range(numCourses)}
        
        for course,prereq in prerequisites:
            hashmap[course].append(prereq)
        print(hashmap)
        visited = set()

        def dfs(course):
            print(course)
            print(visited)
            if course in visited:
                return False
            if hashmap[course] == []:
                return True

            visited.add(course)
            for prereq in hashmap[course]:
                if not dfs(prereq):
                    return False
        
            visited.remove(course)
            hashmap[course] = []
            return True
        
        for c,p in prerequisites:
            if not dfs(c):
                return False
        
        return True

        