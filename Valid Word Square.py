class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """
    def validWordSquare(self, words):
        index = 0
        n = len(words)
        while index < n:
            temp1, temp2 = "", ""
            j = 0
            while j < len(words[index]):
                temp1 += words[index][j]
                j += 1
            for i in range(n):
                if index < len(words[i]):
                    temp2 += words[i][index]
            if temp1 != temp2:
                return False
            index += 1
        return True
        # Write your code here
