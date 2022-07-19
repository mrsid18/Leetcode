class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prereq = [[] for _ in range(numCourses)]
        
        for c,p in prerequisites:
            prereq[c].append(p)
        
        visited =set()
        
        def dfs(c):
            if c in visited:return False
            
            visited.add(c)
            
            for p in prereq[c]:
                if not dfs(p): return False
            
            prereq[c] = []
            visited.remove(c)
            
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        
        return True