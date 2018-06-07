class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        begin = 1
        path, result = [], []
        self.dfs(begin, path, result, n, k)
        return result

    def dfs(self, begin, path, result, n, k):

        if len(path) == k:
            temp = path.copy()
            result.append(temp)
            return

        for i in range(begin, n + 1):
            path.append(i)
            self.dfs(i + 1, path, result, n, k)
            path.pop()
        # write your code here