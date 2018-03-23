class Solution:
    """
    @param str1: a given string
    @param str2: another given string
    @return: An array of missing string
    """
    def missingString(self, str1, str2):
        maxStr = str1 if len(str1) >= len(str2) else str2
        minStr = str1 if len(str1) < len(str2) else str2

        record = maxStr.split()
        temp = minStr.split()
        result = []

        for i in record:
            if i not in temp:
                result.append(i)
        return result
        # Write your code here

