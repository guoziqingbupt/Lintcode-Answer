class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        left, right = n, n
        path, result = [], []
        self.helper(left, right, path, result)
        return result

    def helper(self, left, right, path, result):
        if left == right == 0:
            temp = path.copy()
            result.append(temp)
            return

        if left > 0:
            path.append(0)
            self.helper(left - 1, right, path, result)
            path.pop()

        if right > left:
            path.append(1)
            self.helper(left, right - 1, path, result)
            path.pop()
        # write your code here

obj = Solution()
print(len(obj.generateParenthesis(2)))
