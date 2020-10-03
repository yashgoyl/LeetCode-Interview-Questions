from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (self.is_row_valid(board) and
                self.is_col_valid(board) and
                self.is_subsquare_valid(board))

    def is_row_valid(self,board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True
    
    def is_col_valid(self,board):
        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False
        return True
    
    def is_subsquare_valid(self,board):
        for r in (0,3,6):
            for c in (0,3,6):
                unit = [board[x][y] for x in range(r,r+3) for y in range(c,c+3)]
                # print(unit)
                if not self.is_unit_valid(unit):
                    return False
        return True
    
    def is_unit_valid(self,unit):
        unit_list = [i for i in unit if i != '.']
        return len(set(unit_list)) == len(unit_list)

obj = Solution()
print(obj.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))