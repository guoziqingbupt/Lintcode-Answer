class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if the characters in s can be replaced to get t or false
    """
    def isIsomorphic(self, s, t):
        replaceList = {}
        n, index = len(s), 0

        while index < n:
            if s[index] not in replaceList and t[index] not in replaceList.values():
                replaceList[s[index]] = t[index]
            elif s[index] not in replaceList and t[index] in replaceList.values():
                return False
            elif s[index] in replaceList and replaceList[s[index]] != t[index]:
                return False
            index += 1
        return True
        # write your code here