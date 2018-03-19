class Solution:
    """
    @param s: a string
    @return: it's index
    """
    def firstUniqChar(self, s):
        record = {}
        for i in s:
            if i not in record:
                record[i] = 1
            else:
                record[i] += 1
        index, n = 0, len(s)
        while index < n:
            if record[s[index]] == 1:
                return index
            index += 1
        return -1
        # write your code here
