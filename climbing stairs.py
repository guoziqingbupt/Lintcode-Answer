class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        dp = [1, 2]
        for i in range(3, n + 1):
            dp.append(dp[-1] + dp[-2])
        return dp[-1]
        # write your code here
