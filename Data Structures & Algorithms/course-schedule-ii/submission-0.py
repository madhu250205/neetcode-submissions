class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Step 1: Build the adjacency list where each course points to its prerequisites
        prereq = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
            
        output = []
        # visit: stat = 0 (unvisited), 1 (visiting/current path), 2 (visited)
        visit = [0] * numCourses
        
        def dfs(crs):
            if visit[crs] == 1: # Cycle detected
                return False
            if visit[crs] == 2: # Already processed
                return True
                
            visit[crs] = 1
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
                    
            visit[crs] = 2
            output.append(crs)
            return True
            
        for c in range(numCourses):
            if not dfs(c):
                return []
                
        return output