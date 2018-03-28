class Solution:
    """
    @param n: the given number
    @return: Sum of elements in subsets
    """
    def subSum(self, n):
        result = 0
        num = 0
        for i in range(n, 0, -1):
            result += result + i * num + i
            num = num * 2 + 1

        return result
        # write your code here
