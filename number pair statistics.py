class Solution:
    """
    @param p: the point List
    @return: the numbers of pairs which meet the requirements
    """
    def pairNumbers(self, p):

        c1, c2, c3, c4 = 0, 0, 0, 0

        for ele in p:
            # even and even
            if ele.x % 2 == 0 and ele.y % 2 == 0:
                c1 += 1
            if ele.x % 2 == 0 and ele.y % 2 == 1:
                c2 += 1
            if ele.x % 2 == 1 and ele.y % 2 == 0:
                c3 += 1
            if ele.x % 2 == 1 and ele.y % 2 == 1:
                c4 += 1
        t1, t2, t3, t4 = 0, 0, 0, 0
        if c1 > 1:
            t1 = int(c1 * (c1 - 1) / 2)
        if c2 > 1:
            t2 = int(c2 * (c2 - 1) / 2)
        if c3 > 1:
            t3 = int(c3 * (c3 - 1) / 2)
        if c4 > 1:
            t4 = int(c4 * (c4 - 1) / 2)
        return t1 + t2 + t3 + t4