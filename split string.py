class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        begin = 0
        path = []
        result = []
        self.helper(begin, result, path, s)
        return result

    def helper(self, begin, result, path, s):

        n = len(s)
        cur = begin

        if cur == n:
            temp = path.copy()
            result.append(temp)
            return

        if begin < n:
            path.append(s[cur])
            self.helper(begin + 1, result, path, s)
            path.pop()

        if begin < n - 1:
            path.append(s[cur] + s[cur + 1])
            self.helper(begin + 2, result, path, s)
            path.pop()
        # write your code here
