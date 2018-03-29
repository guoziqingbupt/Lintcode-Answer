class Solution:
    """
    @param num: a positive integer
    @return: if num is a perfect square else False
    """
    def isPerfectSquare(self, num):
        if num == 1:
            return True
        left, right = 0, num // 2

        while left <= right:
            cur = (left + right) // 2
            temp = cur ** 2
            if temp == num:
                return True

            if temp > num:
                right = cur - 1
            else:
                left = cur + 1
        return False
        # write your code here