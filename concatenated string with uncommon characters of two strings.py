class Solution:
    """
    @param s1: the 1st string
    @param s2: the 2nd string
    @return: uncommon characters of given strings
    """
    def concatenetedString(self, s1, s2):
        record = {}
        result = ""

        for char in s2:
            if char not in record:
                record[char] = 1

        for char in s1:
            if char not in record:
                result += char
            else:
                record[char] = 0

        for char in s2:
            if record[char] != 0:
                result += char

        return result
        # write your code here

