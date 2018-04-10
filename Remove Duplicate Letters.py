class Solution:
    """
    @param s: a string
    @return: return a string
    """
    def removeDuplicateLetters(self, s):

        if len(s) == 0:
            return s

        result = s[0]
        index, n = 1, len(s)

        while index < n:
            if s[index] >= result[-1] and s[index] not in result:
                result += s[index]
            elif s[index] not in result:
                while len(result) != 0 and s[index] < result[-1]:
                    if result[-1] in s[index + 1:]:
                        result = result[:-1]
                        continue
                    break
                result += s[index]
            index += 1
        return result
        # write your code here