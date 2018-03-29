class Solution:
    """
    @param matrix: an input matrix
    @return: nums[0]: the maximum,nums[1]: the minimum
    """

    def maxAndMin(self, matrix):
        if len(matrix) == 0:
            return []

        nums = [matrix[0][0], matrix[0][0]]

        for row in matrix:
            for ele in row:
                if ele > nums[0]:
                    nums[0] = ele
                if ele < nums[1]:
                    nums[1] = ele
        return nums
        # write your code here