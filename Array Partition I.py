class Solution:
    """
    @param nums: an array
    @return: the sum of min(ai, bi) for all i from 1 to n
    """
    def arrayPairSum(self, nums):
        nums.sort()
        n = len(nums)
        result = 0
        for i in range(int(n / 2)):
            result += nums[i * 2]
        return result
        # Write your code here
