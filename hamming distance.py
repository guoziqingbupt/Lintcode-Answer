class Solution:
    """
    @param x: an integer
    @param y: an integer
    @return: return an integer, denote the Hamming Distance between two integers
    """
    def hammingDistance(self, x, y):
        s1, s2 = bin(x)[2:], bin(y)[2:]
        n = min(len(s1), len(s2))

        index = -1
        count = 0

        while index >= -n:
            if s1[index] != s2[index]:
                count += 1
            index -= 1
        while index >= -len(s1):
            if s1[index] == "1":
                count += 1
            index -= 1
        while index >= -len(s2):
            if s2[index] == "1":
                count += 1
            index -= 1
        return count
        # write your code here


