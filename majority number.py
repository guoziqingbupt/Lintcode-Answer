class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        if len(nums) == 0:
            return
        majNum = nums[0]
        count = 1
        for ele in nums[1:]:
            if count == 0:
                majNum = ele
                count = 1
            elif ele == majNum:
                count += 1
            else:
                count -= 1
        return majNum
        # write your code here
