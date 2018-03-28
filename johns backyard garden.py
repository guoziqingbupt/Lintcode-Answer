class Solution:
    """
    @param x: the wall's height
    @return: YES or NO
    """
    def isBuild(self, x):
        while x >= 3:
            if x % 3 == 0:
                return "YES"
            x -= 7
        return "NO"
        # write you code here