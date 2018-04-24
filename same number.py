class Solution:
    """
    @param nums: the arrays
    @param k: the distance of the same number
    @return: the ans of this question
    """
    def sameNumber(self, nums, k):
        record = {}
        index, n = 0, len(nums)

        while index < n:
            if nums[index] not in record:
                record[nums[index]] = index
            else:
                if index - record[nums[index]] < k:
                    return "YES"
                else:
                    record[nums[index]] = index
            index += 1
        return "NO"
        # Write your code here
