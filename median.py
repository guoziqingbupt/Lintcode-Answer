class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """
    def median(self, nums):
        begin, end = 0, len(nums) - 1
        target = end // 2

        while begin <= end:
            curOrder = self.helper(begin, end, nums)
            if curOrder == target:
                return nums[target]
            elif curOrder < target:
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
    # write your code here
