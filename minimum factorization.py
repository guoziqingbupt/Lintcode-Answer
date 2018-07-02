class Solution:
    """
    @param a: a positive integer
    @return: the smallest positive integer whose multiplication of each digit equals to a
    """
    def smallestFactorization(self, a):
        minNum, maxNum = 1, 2

        while a > pow(9, minNum):
            minNum += 1

        while a > pow(2, maxNum):
            maxNum += 1

        result = self.helper(a)
        if result > pow(2, 32) - 1:
            return 0
        return result

    def helper(self, a):
        if a <= 9:
            return a

        temp = []
        for dig in range(2, 10):
            if a % dig == 0:
                left = self.helper(a // dig)
                if left == 0:
                    continue
                temp.append(int(str(dig) + str(left)))
        if len(temp) != 0:
            return min(temp)
        return 0
        # Write your code here

obj = Solution()
print(obj.smallestFactorization(9000000))
