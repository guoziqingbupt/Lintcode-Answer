class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        cur = nums[0]

        index = 0
        while index < len(nums):
            count = 0
            while index < len(nums) and cur == nums[index]:
                count += 1
                if count > 2:
                    nums.remove(nums[index])
                else:
                    index += 1
            if index < len(nums):
                cur = nums[index]
        return len(nums)
        # write your code here

