class Solution:
    """
    @param nums: the num arrays
    @return: the num arrays after rearranging
    """
    def rearrange(self, nums):
        nums.sort()
        n = len(nums) - 1

        mid = n // 2 + 1
        right = mid
        left = 0

        result = []
        while right <= n:
            result.append(nums[left])
            result.append(nums[right])
            left += 1
            right += 1
        return result
        # Write your code here
