class Solution:
    """
    @param num: the given number
    @return: whether whether there're two integers
    """
    def checkSumOfSquareNumbers(self, num):

        cur = 0

        while cur <= num:
            if num - cur ** 2 < 0:
                return False
            temp = int((num - cur ** 2) ** 0.5)
            if temp ** 2 + cur ** 2 == num:
                return True
            cur += 1
        return False
        # write your code here


