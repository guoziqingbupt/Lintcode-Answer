class Solution:
    """
    @param g: children's greed factor
    @param s: cookie's size
    @return: the maximum number
    """
    def findContentChildren(self, g, s):
        g.sort(reverse=True)
        s.sort(reverse=True)

        index1, index2 = 0, 0
        n1, n2 = len(g), len(s)

        count = 0
        while index1 < n1 and index2 < n2:
            if g[index1] <= s[index2]:
                count += 1

                index1 += 1
                index2 += 1
            else:
                index1 += 1
        return count
        # Write your code here

