class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        #this is a graph traversal problem
        # for every graph traversal problem, you need a visited
        
        visited = set()
        rows, cols = len(image), len(image[0])
        
        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or (r,c) in visited:
                return
            
            visited.add((r,c))
            image[r][c]=newColor
            directions = [[1,0], [0, 1], [-1, 0], [0, -1]]
            
            for dr, dc in directions:
                if (r+dr) in range(rows) and (c+dc) in range(cols) and image[r+dr][c+dc]==target:
                    dfs(r+dr, c+dc)
        
        target=image[sr][sc]
        dfs(sr, sc)
        return image
            