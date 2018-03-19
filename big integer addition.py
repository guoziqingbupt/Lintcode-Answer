class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return sum of num1 and num2
    """
    def addStrings(self, num1, num2):

        if len(num1) < len(num2):
            shortnum, longnum = num1, num2
        else:
            shortnum, longnum = num2, num1

        n1, n2 = len(shortnum), len(longnum)
        index = -1
        result = ""
        temp = 0

        while index >= -n1:
            cur = int(shortnum[index]) + int(longnum[index]) + temp
            if cur // 10 == 1:
                temp = 1
            else:
                temp = 0
            result = str(cur % 10) + result
            index -= 1

        while index >= -n2:
            cur = int(longnum[index]) + temp
            if cur // 10 == 1:
                temp = 1
            else:
                temp = 0
            result = str(cur % 10) + result
            index -= 1

        if temp == 1:
            result = str(temp) + result
        return result
        # write your code here
