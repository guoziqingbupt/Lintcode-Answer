class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):

        if len(A) == 0:
            return 0

        result1, result2 = 1, 1
        cur1, cur2 = 1, 1

        n = len(A)
        index = 1

        while index < n:
            if A[index] > A[index - 1]:
                cur1 += 1
                cur2 = 1
                result1 = max(cur1, result1)
            elif A[index] < A[index - 1]:
                cur2 += 1
                cur1 = 1
                result2 = max(cur2, result2)
            index += 1
        return max(result1, result2)
        # write your code here
