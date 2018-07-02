class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """

    def topk(self, nums, k):
        self.helper(nums, k, 0, len(nums) - 1)

        return sorted(nums[:k], reverse=True)

    def helper(self, nums, k, begin, end):
        prev = nums[begin]
        left = begin + 1
        right = end
        while left <= right:
            if nums[left] < prev:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        nums[right], nums[begin] = nums[begin], nums[right]

        if right + 1 == k:
            return
        elif right + 1 > k:
            return self.helper(nums, k, begin, right - 1)
        else:
            return self.helper(nums, k, right + 1, end)
        # write your code here