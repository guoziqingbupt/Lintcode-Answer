class Solution:
    """
    @param s: a string
    @return: nothing
    """
    def validPalindrome(self, s):
        left, right = 0, len(s) - 1

        while left <= right:
            if s[left] != s[right]:

                # delete left
                s1 = s[:left] + s[left + 1: right]
                r1 = self.helper(s1)
                if r1:
                    return True

                # delete right
                s2 = s[left:right]
                r2 = self.helper(s2)
                return r2
            left += 1
            right -= 1
        return True

    def helper(self, s):
        left, right = 0, len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
        # Write your code here