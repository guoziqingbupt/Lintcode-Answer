class Solution:
    """
    @param a: the given number
    @param b: another number
    @return: the greatest common divisor of two numbers
    """
    def gcd(self, a, b):
        x1 = max(a, b)
        x2 = min(a, b)

        while x2 != 0:
            temp = x1
            x1 = x2
            x2 = temp % x2
        return x1
        # write your code here