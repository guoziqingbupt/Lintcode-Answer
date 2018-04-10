class Solution:
    """
    @param grid: an integer matrix
    @return: an integer
    """
    def numIslandCities(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        index1, index2 = 0, 0
        row_num, col_num = len(grid), len(grid[0])

        count = 0

        while index1 < row_num:
            index2 = 0
            while index2 < col_num:
                if grid[index1][index2] == 2:
                    count += 1
                    self.dfs(grid, index1, index2)
                index2 += 1
            index1 += 1
        return count

    def dfs(self, grid, i, j):
        if grid[i][j] == 0:
            return
        if grid[i][j] != 0:
            grid[i][j] = 0

        if i + 1 < len(grid):
            self.dfs(grid, i + 1, j)

        if i - 1 >= 0:
            self.dfs(grid, i - 1, j)

        if j + 1 < len(grid[0]):
            self.dfs(grid, i, j + 1)

        if j - 1 >= 0:
            self.dfs(grid, i, j - 1)
        # Write your code here


