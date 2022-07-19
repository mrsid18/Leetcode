class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        points = []
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0: points.append([i,j])
        
        for row, col in points:
            matrix[row] = [0]*cols
            for i in range(rows):
                matrix[i][col] = 0
        