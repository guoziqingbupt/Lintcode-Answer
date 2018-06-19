class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        result = 0
        for i in A:
            result ^= i
        return result
        # write your code here
