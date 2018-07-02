class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        if len(A) == 0:
            return 0
        if len(A) == 1:
            return A[0]
        dp = [A[0], max(A[0], A[1])]
        n = len(A)
        for i in range(2, n):
            dp.append(max(dp[i - 1], dp[i - 2] + A[i]))

        return dp[-1]
        # write your code here
