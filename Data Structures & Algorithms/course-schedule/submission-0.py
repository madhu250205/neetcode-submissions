class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Build an adjacency list mapping each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        # Visit set to track courses along the current DFS path (detects cycles)
        visitSet = set()
        
        def dfs(crs):
            # Base case 1: If we encounter a course already in the current path, we found a cycle
            if crs in visitSet:
                return False
            # Base case 2: If the course has no prerequisites, it can be successfully completed
            if preMap[crs] == []:
                return True
                
            visitSet.add(crs)
            
            # Recursively check all prerequisites for the current course
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
                    
            visitSet.remove(crs)
            preMap[crs] = []  # Memoization: clear prerequisites so we don't re-check
            return True
            
        # Check every course to handle disconnected graphs
        for c in range(numCourses):
            if not dfs(c):
                return False
                
        return True
        