class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = defaultdict(list)
        for prereq, course in prerequisites:
            adj_list[course].append(prereq)
        
        def dfs(course, target_prereq, visited):
            if course in visited:
                return False
            visited.add(course)
            
            for prereq in adj_list[course]:
                if prereq == target_prereq:
                    return True
                if dfs(prereq, target_prereq, visited):
                    return True
            return False
        
        res = []
        for u, v in queries:
            # Is u a prerequisite of v?
            res.append(dfs(v, u, set()))
        
        return res