class Solution:
    """
    @param num: a non-negative integer
    @return: one digit
    """
    def addDigits(self, num):
        result = num
        while result // 10 != 0:
            temp = sum([int(i) for i in str(result)])
            result = temp
        return result
        # write your code here