class Solution:
    """
    @param n: a Integer
    @return: a spiral array
    """
    def spiralArray(self, n):

        start = 1
        index = 0
        result = [[0 for col in range(n)] for row in range(n)]

        self.helper(start, index, n, result)

        return result

    def helper(self, start, index, n, result):

        if index == n:
            return

        # to right
        for i in range(index, n - index):
            result[index][i] = start
            start += 1

        # to down
        for i in range(index + 1, n - index):
            result[i][n - index - 1] = start
            start += 1

        # to left
        for i in range(n - 2 - index, index - 1, -1):
            result[n - 1 - index][i] = start
            start += 1

        # to up
        for i in range(n - 2 - index, index, -1):
            result[i][index] = start
            start += 1

        self.helper(start, index + 1, n, result)
        # write your code here
