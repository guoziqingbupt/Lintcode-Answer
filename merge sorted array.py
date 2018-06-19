class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        index1, index2 = m - 1, n - 1
        cur = m + n - 1
        while index1 >= 0 and index2 >= 0:
            if A[index1] >= B[index2]:
                A[cur] = A[index1]
                index1 -= 1
            else:
                A[cur] = B[index2]
                index2 -= 1
            cur -= 1
        if index2 >= 0:
            A[:cur + 1] = B[:cur + 1]
        return A
        # write your code here


