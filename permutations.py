class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        temp = nums[:]
        n = len(nums)
        path, result = [], []
        if len(nums) == 0:
            result.append(path)
            return result
        self.helper(temp, path, n, result)
        return result

    def helper(self, temp, path, n, result):

        index = 0
        while index < len(temp):
            cur = temp[index]
            path.append(cur)

            if len(path) == n:
                result.append(path[:])
                path.pop()
                return

            temp.remove(cur)
            self.helper(temp, path, n, result)
            temp.insert(index, cur)
            path.pop()
            index += 1
        # write your code here

obj = Solution()
print(len(obj.permute([1, 2, 3, 4])))