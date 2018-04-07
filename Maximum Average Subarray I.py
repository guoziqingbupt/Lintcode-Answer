class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: the maximum average value
    """
    def findMaxAverage(self, nums, k):
        result = sum(nums[:k])
        n = len(nums)
        left, right = 0, k

        temp = result
        while right < n:
            temp = temp - nums[left] + nums[right]
            if result < temp:
                result = temp
            left += 1
            right += 1
        return result / k
        # Write your code here

obj = Solution()
nums = [4,2,1,3,3]
print(obj.findMaxAverage(nums, 2))
