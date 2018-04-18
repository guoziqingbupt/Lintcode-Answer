class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """
    def generatePossibleNextMoves(self, s):
        result = []
        if len(s) == 0:
            return result

        index, n = 0, len(s)
        while index < n - 1:
            if s[index: index + 2] == "++":
                result.append(s[:index] + "--" + s[index + 2:])
            index += 1
        return result
        # write your code here