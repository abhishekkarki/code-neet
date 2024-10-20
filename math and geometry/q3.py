# https://neetcode.io/problems/set-zeroes-in-matrix
# Medium

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        rowzero = False
        
        for i in range(m):
            for j in range(n):
                if i == 0 and matrix[i][j] == 0:
                    rowzero = True
                elif matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        #print(matrix)
        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        
        #print(matrix)
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        #print(matrix)
        #print(rowzero, matrix[0][0])
        if matrix[0][0] == 0:
            for i in range(1, m):
                matrix[i][0] = 0
        if rowzero:
            for j in range(n):
                matrix[0][j] = 0