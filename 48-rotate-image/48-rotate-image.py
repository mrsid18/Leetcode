class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        matrix.reverse()
        visited = set()
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if (i,j) not in visited and (j, i) not in visited:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                    visited.add((i, j))
               