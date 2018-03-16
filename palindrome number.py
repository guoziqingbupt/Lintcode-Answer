class Solution:
    """
    @param num: a positive number
    @return: true if it's a palindrome or false
    """

    def isPalindrome(self, num):
        index = 0
        n = len(str(num))

        while index <= n - 1 - index:
            if str(num)[index] != str(num)[n - 1 - index]:
                return False
            index += 1

        return True
        # write your code here
