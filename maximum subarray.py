class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0
        dp = [nums[0]]
        index, n = 1, len(nums)
        while index < n:
            if dp[-1] < 0:
                dp.append(nums[index])
            else:
                dp.append(nums[index] + dp[-1])
            index += 1
        return max(dp)
        # write your code here
