class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        result = nums[0]
        count = 1
        for i in nums[1:]:
            if count == 0:
                result = i
                count = 1
            elif i == result:
                count += 1
            else:
                count -= 1
        return result
        # write your code here