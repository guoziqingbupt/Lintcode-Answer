class Solution:
    """
    @param board: the board
    @return: whether the Sudoku is valid
    """
    def isValidSudoku(self, board):
        tableRow = [[] for j in range(9)]
        tableCol = [[] for j in range(9)]
        tableCube = [[] for j in range(9)]

        for row_num in range(9):
            for col_num in range(9):

                temp = board[row_num][col_num]
                if temp == ".":
                    continue
                temp = int(temp)

                if temp in tableRow[row_num] or temp in tableCol[col_num] or \
                                temp in tableCube[(row_num // 3) * 3 + (col_num // 3)]:
                    return False
                else:
                    tableRow[row_num].append(temp)
                    tableCol[col_num].append(temp)
                    tableCube[(row_num // 3) * 3 + (col_num // 3)].append(temp)
        return True
        # write your code here