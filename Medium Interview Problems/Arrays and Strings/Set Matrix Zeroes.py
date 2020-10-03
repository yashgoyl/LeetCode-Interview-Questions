class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        
        rcz = set()
        ccz = set()
        
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    rcz.add(i)
                    ccz.add(j)
                    
        for row in rcz:
            for column in range(c):
                matrix[row][column] = 0
                
        for col in ccz:
            for row in range(r):
                matrix[row][col] = 0
            
        return matrix
