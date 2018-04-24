class Solution:
    """
    @param s: s string
    @return: return an integer, denote the number of the palindromic substrings
    """
    def countPalindromicSubstrings(self, s):
        index, n = 0, len(s)
        result = 0
        while index < n:
            result += 1
            # odd
            left = index - 1
            right = index + 1
            while left >= 0 and right < n and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1

            # even
            left = index
            right = index + 1
            while left >= 0 and right < n and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1

            index += 1
        return result
        # write your code here
