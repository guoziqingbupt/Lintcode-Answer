class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        dict = list(dict)
        index, n = 0, len(s)

        while index < n:
            flag = False
            for word in dict:
                count = len(word)
                if s[index: index + count] == word:
                    index += count
                    flag = True
            if not flag:
                return False
        return True
        # write your code here

