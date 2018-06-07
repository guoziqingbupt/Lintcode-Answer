class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        if n == 0:
            return 0

        rowIndex, colIndex = 0, len(matrix[0]) - 1

        count = 0
        while rowIndex < n and colIndex >= 0:
            if matrix[rowIndex][colIndex] == target:
                count += 1
                if rowIndex < n - 1:
                    rowIndex += 1
                elif colIndex > 0:
                    colIndex -= 1
                else:
                    return count
            if matrix[rowIndex][colIndex] > target:
                colIndex -= 1
            else:
                rowIndex += 1
        return count
        # write your code here
