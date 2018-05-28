class Solution:
    """
    @param num: the given number
    @return: The base 7 string representation
    """
    def convertToBase7(self, num):
        if num >= 0:
            return self.helper(num)
        else:
            return "-" + self.helper(abs(num))

    def helper(self, num):
        result = ""
        index = 1
        while num > 0:
            cur = (num % pow(7, index)) // pow(7, index - 1)
            num -= cur * pow(7, index - 1)
            index += 1
            result = str(cur) + result
        return result
        # Write your code here
