class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols  = len(matrix[0])
        row_list = list()
        col_list = list()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    row_list.append(i)
                    col_list.append(j)

        for row_value in row_list:
            for c in range(cols):
                matrix[row_value][c] = 0

        for col_value in col_list:
            for r in range(rows):
                matrix[r][col_value] = 0
        
            
        
        