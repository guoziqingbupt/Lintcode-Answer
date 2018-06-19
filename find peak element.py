class Solution:
    """
    @param: A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) // 2
            if A[mid - 1] < A[mid] and A[mid] > A[mid + 1]:
                return mid
            elif A[mid] < A[mid + 1]:
                left = mid + 1
            elif A[mid - 1] > A[mid]:
                right = mid - 1
        # write your code here
