class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """

    def uniquePaths(self, m, n):
        if m < 1 or n < 1:
            return 0
        record = [[1 for i in range(n)] for j in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                record[row][col] = record[row - 1][col] + record[row][col - 1]
        return record[-1][-1]