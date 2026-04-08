class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = defaultdict(list)
        for prereq, course in prerequisites:
            adj_list[course].append(prereq)
        
        prereqMap = {}

        def dfs(course):
            #WHY DO WE NEED THIS
            if course not in prereqMap:
                prereqMap[course] = set()
                for pre in adj_list[course]:
                    prereqMap[course] |= dfs(pre)
                
                prereqMap[course].add(course)
            return prereqMap[course]

        for n in range(numCourses):
            dfs(n)
        
        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])
        
        return res

        
        # print(prereqMap)