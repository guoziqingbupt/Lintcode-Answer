class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        count = 0
        while n != 0:
            n //= 5
            count += n
        return count
        # write your code here, try to do it without arithmetic operators.
