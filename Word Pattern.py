class Solution:
    """
    @param pattern: a string, denote pattern string
    @param str: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """
    def wordPattern(self, pattern, str):
        record = {}
        temp = str.split()
        index, n = 0, len(pattern)
        if n != len(temp):
            return False
        while index < n:
            if pattern[index] not in record:
                if temp[index] in record.values():
                    return False
                else:
                    record[pattern[index]] = temp[index]
            elif record[pattern[index]] != temp[index]:
                return False
            index += 1
        return True
        # write your code here

