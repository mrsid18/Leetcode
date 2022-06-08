class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # basically this is graph traversal problem
        # 1->t,r,b,l
        if not grid:
            return 0
        
        cols, rows = len(grid[0]), len(grid)
        
        visited = set() #(m,n)
        
        res = 0
        
        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or grid[r][c]=='0' or (r,c) in visited:
                return
            
            visited.add((r,c))
            directions = [[1,0],[0,1],[-1,0], [0,-1]]
            
            for dr, dc in directions:
                dfs(r+dr, c+dc)
                # if grid[r+dr][c+dc]=='1' and (r+dr, c+dc) not in visited:
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1' and (r,c) not in visited:
                    res+=1
                    dfs(r,c)
        
        return res
        
        
        