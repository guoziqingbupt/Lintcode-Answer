class Solution:
    """
    @param: : A string
    @param: : A string
    @return: Count the number of distinct subsequences
    """

    def numDistinct(self, S, T):
        dp = [[0 for i in range(len(S) + 1)] for j in range(len(T) + 1)]
        for i in range(len(S) + 1):
            dp[0][i] = 1
        for i in range(1, len(T) + 1):
            for j in range(1, len(S) + 1):
                if S[j - 1] == T[i - 1]:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[len(T)][len(S)]
        # write your code here