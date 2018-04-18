class Solution:
    """
    @param str: The input string
    @return: The answer
    """
    def dataSegmentation(self, s):
        index, n = 0, len(s)
        result = []

        if n == 0:
            return result
        while index < n:
            if s[index] == " ":
                index += 1
                continue
            if not s[index].isalpha():
                result.append(s[index])
                index += 1
                continue
            cur = ""
            while index < n and s[index].isalpha():
                cur += s[index]
                index += 1
            result.append(cur)
        return result
        # Write your code here

