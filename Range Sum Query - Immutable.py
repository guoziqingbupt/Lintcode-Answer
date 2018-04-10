class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = nums
        index, n = 1, len(nums)

        while index < n:
            self.dp[index] += self.dp[index - 1]
            index += 1

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.dp[j]
        return self.dp[j] - self.dp[i - 1]
        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # param_1 = obj.sumRange(i,j)
