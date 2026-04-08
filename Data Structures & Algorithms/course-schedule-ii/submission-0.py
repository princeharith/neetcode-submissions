class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        class_to_req_map = {c: [] for c in range(numCourses)}

        for a,b in prerequisites:
            class_to_req_map[a].append(b)

        current_cycle = set()
        visited = set()
        res = []

        def dfs(course):
            if course in current_cycle:
                return False
            if course in visited:
                return True
            current_cycle.add(course)
            
            for prereq in class_to_req_map[course]:
                if dfs(prereq) == False:
                    return False

            current_cycle.remove(course)
            visited.add(course)
            res.append(course)

            return True


        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        
        return res



        