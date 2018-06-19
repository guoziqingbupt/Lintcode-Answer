class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        left, right = 0, len(A) - 1

        while left <= right:
            mid = (left + right) // 2
            if A[mid] == target:
                return mid
            if A[mid] > A[left]:
                if A[mid] > target >= A[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if A[mid] < target <= A[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
        # write your code here
