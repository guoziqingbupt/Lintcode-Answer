class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        up, down = 0, len(matrix) - 1
        if down >= 0:
            left, right = 0, len(matrix[0]) - 1

        while up <= down:
            rowMidIndex = (up + down) // 2
            if matrix[rowMidIndex][right] >= target >= matrix[rowMidIndex][left]:
                while left <= right:
                    colMidIndex = (left + right) // 2
                    if matrix[rowMidIndex][colMidIndex] == target:
                        return True
                    if matrix[rowMidIndex][colMidIndex] > target:
                        right = colMidIndex - 1
                    else:
                        left = colMidIndex + 1
                return False
            if matrix[rowMidIndex][left] > target:
                down = rowMidIndex - 1
            else:
                up = rowMidIndex + 1
        return False
        # write your code here