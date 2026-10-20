class Solution:
    def isValidSudoku(self, board):

        for row in range(9):

            for col in range(9):

                if board[row][col]!=".":
                    character = board[row][col]

                    if not self.check_no_row_duplicate(board,row,col,character) or    not               self.check_no_col_duplicate(board,row,col,character) or self.box_has_duplicate(board,row,col,character):
                        return False
        return True


    def check_no_row_duplicate(self,board,row,col,char):

        for i in range(9):
            if i!=col and char==board[row][i]:
                return False

        return True

    def check_no_col_duplicate(self,board,row,col,char):

        for i in range(9):
            if i!=row and char==board[i][col]:
                return False

        return True

    def box_has_duplicate(self, board, row, col, char):
        start_r = (row // 3) * 3
        start_c = (col // 3) * 3
        for r in range(start_r, start_r + 3):
            for c in range(start_c, start_c + 3):
                if (r, c) != (row, col) and board[r][c] == char:
                    return True
        return False

