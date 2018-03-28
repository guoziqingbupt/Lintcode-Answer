class Solution:
    """
    @param n: a Integer
    @return: the first n-line Yang Hui's triangle
    """
    def calcYangHuisTriangle(self, n):
        result = []

        if n == 0:
            return result

        cur = 1
        result.append([1])
        while cur < n:

            if n == 1:
                return result

            item = [1]
            index = 0
            while index < cur - 1:
                item.append(result[-1][index] + result[-1][index + 1])
                index += 1
            item.append(1)
            result.append(item)
            cur += 1

        return result
        # write your code here

