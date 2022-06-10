class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        #this is graph traversal problem
        
        visited = set()
        val = image[sr][sc]
        rows,cols = len(image), len(image[0])
        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or (r,c) in visited or image[r][c]!=val:
                return
            
            visited.add((r,c))
            image[r][c] = newColor
            
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            
            for dr,dc in directions:
                dfs(r+dr, c+dc)
        
        dfs(sr,sc)
        return image
                
            
            