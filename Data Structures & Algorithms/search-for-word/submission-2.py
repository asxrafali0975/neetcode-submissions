class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        for i in range(row):
            for j in range(col):
                if board[i][j]==word[0]:
                    if self.start(board,i,j,row,col,1,word)==True:
                        return True
        return False

    def start(self,board,i,j,row,col,index,word):
        if len(word)==index:                      
            return True

        temp = board[i][j]                     
        board[i][j] = '#'


        #left check
        if j-1>=0:
            if board[i][j-1]==word[index]:      
                if self.start(board,i,j-1,row,col,index+1,word)==True:
                    return True

        #right check
        if j+1<col:
            if board[i][j+1]==word[index]:
                if self.start(board,i,j+1,row,col,index+1,word)==True:
                    return True

        #up check
        if i-1>=0:
            if board[i-1][j]==word[index]:
                if self.start(board,i-1,j,row,col,index+1,word)==True:
                    return True

        #down check
        if i+1<row:
            if board[i+1][j]==word[index]:
               if  self.start(board,i+1,j,row,col,index+1,word)== True:
                return True

        board[i][j] = temp                        
        return False