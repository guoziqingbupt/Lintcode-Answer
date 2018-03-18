class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        return n != 0 and not n & (n - 1)
        # write your code here
