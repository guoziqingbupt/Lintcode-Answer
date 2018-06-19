class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        if len(A) == 0:
            return
        begin, end = 0, len(A) - 1
        while begin <= end:
            curOrder = self.helper(begin, end, A)
            if curOrder == len(A) - k:
                return A[curOrder]
            elif curOrder < len(A) - k:
                begin = curOrder + 1
            else:
                end = curOrder - 1
        return

    def helper(self, begin, end, A):
        if end - begin == 0:
            return begin

        prev = A[begin]
        left, right = begin + 1, end
        while left <= right:
            if A[left] > prev:
                A[left], A[right] = A[right], A[left]
                right -= 1
            else:
                left += 1
        A[left - 1], A[begin] = A[begin], A[left - 1]
        return left - 1