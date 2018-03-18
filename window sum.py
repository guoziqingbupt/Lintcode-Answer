class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):

        if k == 0:
            return []

        n = len(nums)
        firstIndex = 0
        result = [sum(nums[firstIndex:firstIndex + k])]
        if n <= k:
            return result

        lastIndex = k - 1
        while lastIndex + 1 < n:
            cur = result[-1] - nums[firstIndex] + nums[lastIndex + 1]
            result.append(cur)
            firstIndex += 1
            lastIndex += 1
        return result
        # write your code here