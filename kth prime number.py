class Solution:
    """
    @param n: the number
    @return: the rank of the number
    """
    def kthPrime(self, n):
        record = [True for i in range(n)]

        record[0] = False
        index1 = 1

        while index1 < n:
            if not record[index1]:
                index1 += 1
                continue
            elif self.isPrime(index1 + 1):
                times = 2
                while times * (index1 + 1) <= n:
                    record[times * (index1 + 1) - 1] = False
                    times += 1
                index1 += 1

        return sum([i for i in record if i])

    def isPrime(self, num):
        end = int(num ** 0.5)
        for i in range(2, end):
            if num % 2 == 0:
                return False
        return True
        # write your code here
