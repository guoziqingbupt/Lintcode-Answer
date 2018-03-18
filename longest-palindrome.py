class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        record = []
        result = 0

        for char in s:
            if char in record:
                result += 2
                record.remove(char)
            else:
                record.append(char)
        if len(record) != 0:
            result += 1
        return result
        # write your code here
