class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """

    def longestCommonPrefix(self, strs):

        maxLen = 0
        result = ""
        for s in strs:
            curLen = len(s)
            if curLen > maxLen:
                maxLen = curLen
                result = s

        for s in strs:
            index = 0
            while index < len(s):
                if s[index] != result[index]:
                    break
                index += 1
            maxLen = min(index, maxLen)

        return result[: maxLen]
        # write your code here


