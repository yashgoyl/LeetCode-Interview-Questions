from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix[0])
        
        #--1.---Using New Memory----

        # new_matrix = []
        # for col in zip(*matrix):
        #     col1 = list(col)
        #     new_matrix.append(col1)
        # # print(new_matrix)
        # for i in range(n):
        #     new_matrix[i].reverse()
        # return new_matrix

        #-------OR---2.-----Using Same Memory----

        # matrix = list(zip(*matrix))
        # for i in range(n):
        #     matrix[i] = list(matrix[i])
        # for i in range(n):
        #     matrix[i].reverse()
        # return matrix

        #-------OR----3.----Using Transpose----  

        for row in range(n):
            for col in range(row,n):
                matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]

        for i in range(n):
            matrix[i].reverse() 
        return matrix
            

obj = Solution()
print(obj.rotate([
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]))