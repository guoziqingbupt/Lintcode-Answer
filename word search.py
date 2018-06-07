class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):



        count = 0
        path = [(0, 0)]
        for i in range(rowNum):
            for j in range(colNum):
                if board[i][j] == word[count]:
                    path.append((i, j))
                    count += 1

    def helper(self, path, board, curWord):

        rowNum = len(board)
        colNum = len(board[0])

        curPos = path[-1][0]

        if 0 <= path[-1][0] - 1 and (curPos[0] - 1, curPos[1]) not in path:
            if board[curPos[0] - 1][curPos[1]] == curWord[0]:
                curWord

        if board[path[-1][0] + 1][path[-1][1]]

        if board[path[-1][0]][path[-1][1] - 1]

        if board[path[-1][0]][path[-1][1] + 1]


        # write your code here
