class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """

    def removeDuplicates(self, nums):
        index = 1
        if len(nums) == 0:
            return 0

        cur = nums[0]
        while index < len(nums):
            if nums[index] == cur:
                nums.pop(index)
            else:
                cur = nums[index]
                index += 1
        return len(nums)
        # write your code here
