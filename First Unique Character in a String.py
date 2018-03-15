class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """

    def firstUniqChar(self, str):
        candidateList = []
        blackList = []
        for char in str:

            if char not in candidateList and char not in blackList:
                candidateList.append(char)

            elif char in blackList:
                continue

            elif char in candidateList:
                blackList.append(char)
                candidateList.remove(char)

        return candidateList[0]
        # Write your code here