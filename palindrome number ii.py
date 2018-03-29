class Solution:
    """
    @param n: non-negative integer n.
    @return: return whether a binary representation of a non-negative integer n is a palindrome.
    """
    def isPalindrome(self, n):

        temp = self.binaryTrans(n)
        left, right = 0, len(temp) - 1
        while left <= right:
            if temp[left] != temp[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

    def binaryTrans(self, num):
        if num == 0:
            return "0"

        result = ""
        while num // 2 != 0:
            temp = num % 2
            result = str(temp) + result
            num //= 2
        result = "1" + result
        return result
        # Write your code here