class Solution:
    """
    @param n: the number n
    @return: the times n convert to 1
    """
    def digitConvert(self, n):
        count = 0
        while n != 1:
            count += 1
            if n % 2 == 0:
                n //= 2
            elif n % 2 == 1:
                n = 3 * n + 1
        return count
        # Write your code here
