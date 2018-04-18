class Solution:
    """
    @param str: a string
    @return: a compressed string
    """
    def compress(self, s):
        if len(s) == 0:
            return ""

        index, n = 0, len(s)
        result = ""

        while index < n:
            cur = s[index]
            count = 0
            while index < n and s[index] == cur:
                count += 1
                index += 1
            result += (cur + str(count))

        if len(s) <= len(result):
            return s
        return result
        # write your code here

