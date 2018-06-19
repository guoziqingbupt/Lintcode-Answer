class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        result = ""
        index, n = 0, len(s)
        while index < n:
            if s[index] == " ":
                index += 1
                continue

            count = 0
            temp = index
            while index < n and s[index] != " ":
                count += 1
                index += 1
            result = s[temp: temp + count] + " " + result
        return result[:-1]
        # write your code here

