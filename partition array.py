class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        left, right = 0, len(nums) - 1
        if right < 0:
            return 0
        while left < right:
            if nums[left] >= k:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        if nums[right] >= k:
            return right
        else:
            return right + 1
        # write your code here
